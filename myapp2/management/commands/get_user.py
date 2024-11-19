# Извлечение одного пользователя использование фильтра pk первичный ключ аналог id
# Фильтрация объектов модели
# Для фильтрации объектов модели по заданным условиям можно использовать метод filter():
# Model.objects.filter(param__filter=value)
# Фреймворк Django
# exact - точное совпадение значения поля
# iexact - точное совпадение значения поля без учета регистра
# contains - значение поля содержит заданный подстроку
# in - значение поля находится в заданном списке значений
# gt - значение поля больше заданного значения
# gte - значение поля больше или равно заданному значению
# lt - значение поля меньше заданного значения
# lte - значение поля меньше или равно заданному значению
# startswith - значение поля начинается с заданной подстроки
# endswith - значение поля заканчивается на заданную подстроку
# range - значение поля находится в заданном диапазоне значений
# date - значение поля является датой, соответствующей заданной дате
# year - значение поля является годом, соответствующим заданному году


from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get user by id."

    # def add_arguments(self, parser):
    #     parser.add_argument('id', type=int, help='User ID')
    #
    # def handle(self, *args, **kwargs):
    #     id = kwargs['id']
    #     user = User.objects.get(id=id)
    #     self.stdout.write(f'{user}')

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()  # .first() получить первого usera если их несколько
        self.stdout.write(f'{user}')
