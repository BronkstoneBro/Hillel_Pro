import random
from django.core.management.base import BaseCommand
from faker import Faker
from catalog.models import Category, Goods

class Command(BaseCommand):
    help_text = 'Команда для заполнения Базы Данных'
    def handle(self, *args, **options):
        fake = Faker()
        print('Start')
        for _ in range(15):
            cat_name = fake.job
            print(f'Категория {cat_name}')
            category, created = Category.objects.get_or_create(
                name = cat_name(),
                url = fake.url(),
                description = fake.paragraph(nb_sentences=3),
                activate = fake.pybool(),
            )
            for _ in range(random.randint(3,7)):
                goods_name = fake.name()
                print(f'Товар: {goods_name}')
                Goods.objects.create(
                    name=goods_name,
                    description = fake.paragraph(nb_sentences=4),
                    price= random.randint(500,2500),
                    activate=fake.pybool(),
                    category= category,
                    image=fake.image_url(),

                )

        print('Finish')