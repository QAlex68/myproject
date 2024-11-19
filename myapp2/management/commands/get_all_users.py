# Получение объектов модели, read Для получения объектов модели из базы данных можно
# использовать методы .all(), .get(), .filter()
# Фреймворк Django
# ● all() возвращает все объекты модели
# ● get() возвращает один объект, соответствующий заданным условиям
# ● filter() возвращает объекты подходящие под условия фильтрации


from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')
