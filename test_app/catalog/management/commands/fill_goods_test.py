import random
import requests
from django.core.management.base import BaseCommand
from catalog.models import Category, Goods

class Command(BaseCommand):
    help_text = 'Команда для заполнения Базы Данных'

    API_URL = 'https://api.escuelajs.co/api/v1/products'

    def handle(self, *args, **options):
        response = requests.get(self.API_URL)
        if response.status_code == 200:
            data = response.json()
            print('Start')
            for item in data:
                cat_name = item['category']['name']
                print(f'Категория {cat_name}')
                category, created = Category.objects.get_or_create(
                    name=cat_name,
                    defaults={'image': item['category'].get('image', '')},
                )
                if created:
                    print(f'Категория {cat_name} создана')
                for _ in range(random.randint(3, 7)):
                    goods_name = item['title']
                    print(f'Товар: {goods_name}')
                    goods, created = Goods.objects.get_or_create(
                        name=goods_name,
                        defaults={
                            'description': item.get('description', ''),
                            'price': item.get('price', random.randint(500, 2500)),
                            'activate': True,
                            'category': category,
                            'image': item['images'][0] if item['images'] else '',
                        }
                    )
                    if created:
                        print(f'Товар {goods_name} создан')

            print('Finish')
        else:
            print(f'Failed to fetch data from API. Status code: {response.status_code}')
