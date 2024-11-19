# Работа с данными в моделях - Создание объектов модели, create
# Для создания нового объекта модели необходимо создать экземпляр класса модели и заполнить его поля значениями.
# Например, чтобы создать нового пользователя, мы можем использовать следующий код в файле
# myapp2/management/commands/make_products.py:


from django.core.management.base import BaseCommand
from s02app.models import Author


class Command(BaseCommand):
    help = "Create Author."

    # name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.EmailField()
    # bio = models.TextField()
    # birthday = models.DateField()

    def handle(self, *args, **kwargs):
        # author = Author(name='Аарон', last_name='Чинганчгук!', email='aaron@gmail.com', bio='злой индеец', birthday='2024-02-03')
        # author = Author(name='Мойша', last_name='Виниту', email='aaron@gmail.com', bio='злой индеец', birthday='2024-02-03')
        # author = Author(name='Сара', last_name='Покахонтас', email='aaron@gmail.com', bio='злой индеец', birthday='2024-02-03')
        author = Author(name='Изя', last_name='Ункас', email='aaron@gmail.com', bio='злой индеец', birthday='2024-02-03')
        author.save()
        self.stdout.write(f'Автор: {author.full_name()} добавлен!')
