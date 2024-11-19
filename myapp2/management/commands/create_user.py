# Работа с данными в моделях - Создание объектов модели, create
# Для создания нового объекта модели необходимо создать экземпляр класса модели и заполнить его поля значениями.
# Например, чтобы создать нового пользователя, мы можем использовать следующий код в файле
# myapp2/management/commands/make_products.py:


from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com', password='secret', age=25)
        # user = User(name='Neo', email='neo@example.com', password='secret', age=58)
        user = User(name='Jack', email='capitan@example.com', password='secret', age=32)
        user.save()
        self.stdout.write(f'{user}')


