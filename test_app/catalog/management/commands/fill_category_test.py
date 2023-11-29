from django.core.management.base import BaseCommand
from catalog.models import Category
import requests


class Command(BaseCommand):
    help_text = 'Команда для заполнения Базы Данных'

    def get_category_api(self):
        URL = 'https://api.escuelajs.co/api/v1/categories'
        req = requests.get(URL)

        if req.status_code == 200:
            data = req.json()
            categories = []
            for category in data:
                name = category.get('name', '')
                url = category.get('url', '')
                description = category.get('description', '')
                activate = category.get('activate', True)
                category_info = {
                    'name': name,
                    'url': url,
                    'description': description,
                    'activate': activate
                }
                categories.append(category_info)
            return categories
        else:
            print(f"Error: {req.status_code}")
            return None

    def handle(self, *args, **options):
        print('Start')

        categories_data = self.get_category_api()

        if categories_data:
            for category_info in categories_data:
                Category.objects.get_or_create(**category_info)

        print('Finish')
