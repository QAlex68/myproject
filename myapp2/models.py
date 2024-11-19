# # Создание моделей. Наиболее часто используемые поля
# На самом деле в Django более трёх полей, которые мы использовали при создании пользователя.
# Кратко рассмотрим десяток самых частых полей.
# 1. CharField - поле для хранения строковых данных. Параметры: max_length (максимальная длина строки), blank
# (может ли поле быть пустым), null (может ли поле содержать значение Null), default (значение по умолчанию).
# 2. IntegerField - поле для хранения целочисленных данных. Параметры: blank, null, default.
# 3. TextField - поле для хранения текстовых данных большой длины. Параметры: blank, null, default.
# 4. BooleanField - поле для хранения логических значений (True/False). Параметры: blank, null, default.
# 5. DateField - поле для хранения даты. Параметры: auto_now (автоматически устанавливать текущую дату при создании
# объекта), auto_now_add (автоматически устанавливать текущую дату при добавлении объекта в базу данных), blank, null, default.
# 6. DateTimeField - поле для хранения даты и времени. Параметры: auto_now, auto_now_add, blank, null, default.
# 7. ForeignKey - поле для связи с другой моделью. Параметры: to (имя модели, с которой устанавливается связь),
# on_delete (действие при удалении связанного объекта), related_name (имя обратной связи).
# 8. ManyToManyField - поле для связи с другой моделью в отношении "многие-ко-многим". Параметры: to, related_name.
# 9. DecimalField - поле для хранения десятичных чисел. Параметры: max_digits (максимальное количество цифр), decimal_places
# (количество знаков после запятой), blank, null, default.
# 10. EmailField - поле для хранения электронной почты. Параметры: max_length, blank, null, default.


from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')


# Внимание! Для использования в моделях Django поля ImageField необходимо установить дополнительный модуль Pillow.
# Выполните команду внутри виртуального окружения проекта: pip install Pillow
# Данная библиотека нужна для работы Python с изображениями.


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

# Как создать миграции для моделей - python manage.py makemigrations myapp2
# Применение миграций - python manage.py migrate


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'


