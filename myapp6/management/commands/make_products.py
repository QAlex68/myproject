# Работа с данными в моделях - Создание объектов модели, create
# Для создания нового объекта модели необходимо создать экземпляр класса модели и заполнить его поля значениями.
# Например, чтобы создать нового пользователя, мы можем использовать следующий код в файле
# myapp3/management/commands/make_products.py:
# python manage.py make_products 10000


from random import choice, randint, uniform
from django.core.management.base import BaseCommand
from myapp5.models import Category, Product


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Кроличество продуктов для генерации')

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        products = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            products.append(Product(name=f'продукт номер {i}',
                                    category=choice(categories),
                                    description='длинное описание продукта, которое и так никто не читает',
                                    price=uniform(0.01, 999_999.99),
                                    quantity=randint(1, 10_000),
                                    rating=uniform(0.01, 9.99),
                                    ))
        Product.objects.bulk_create(products)
