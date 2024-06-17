from django.core.management import BaseCommand
import json

from catalog.models import Category, Product


class Command(BaseCommand):
    @staticmethod
    def json_read_categories():
        with open('category_data.json', encoding='utf-16') as f:
            category_list = json.load(f)
            commands_list = []
            for item in category_list:
                commands_list.append(item)
            return commands_list

    # Здесь мы получаем данные из фикстурв с категориями

    @staticmethod
    def json_read_products():
        with open('product_data.json', encoding='utf-16') as f:
            category_list = json.load(f)
            commands_list = []
            for item in category_list:
                commands_list.append(item)
            return commands_list

    # Здесь мы получаем данные из фикстурв с продуктами

    def handle(self, *args, **options):
        Product.objects.all().delete()
        # Удалите все продукты
        Category.objects.all().delete()
        # Удалите все категории

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'], name=category['fields']['name'],
                         description=category['fields']['description']))

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(Product(id=product['pk'],
                                              category=Category.objects.get(
                                                  pk=product['fields'][
                                                      'category']),
                                              name=product['fields']['name'],
                                              price=product['fields']['price'],
                                              description=product['fields'][
                                                  'description']))

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
