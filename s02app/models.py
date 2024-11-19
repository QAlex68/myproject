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
# Задание №1
# Создайте модель для запоминания бросков монеты: орёл или
# решка.
# Также запоминайте время броска

class CoinFlip(models.Model):
    FLIP_CHOICES = [
        ('H', 'Орел'),
        ('T', 'Решка'),

    ]

    result = models.CharField(max_length=1, choices=FLIP_CHOICES)
    flip_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.result} flipped at {self.flip_time}'

    # Семинар 2Задание № 2
    # Доработаем задачу 1.
    # Добавьте статический метод для статистики по n последним броскам монеты.
    # Метод должен возвращать словарь с парой ключейзначений, для орла и для решки.

    @staticmethod
    def get_last_flips(n):
        flips = CoinFlip.objects.order_by('-flip_time')[:n]
        stats = {'H': 0, 'T': 0}
        for flip in flips:
            if flip.result == 'H':
                stats['H'] += 1
            else:
                stats['T'] += 1
        return stats


# Задание №3
# Создайте модель Автор. Модель должна содержать следующие поля:
# ○ имя до 100 символов
# ○ фамилия до 100 символов
# ○ почта
# ○ биография
# ○ день рождения
# Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def full_name(self):
        return f'{self.name} {self.last_name}'

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'

    # Для отображения в админке
    # class Meta:
    #     verbose_name: str = 'Автор'
    #     verbose_name_plural = 'Авторы'




# Сем 2 задание 4
# Создайте модель Статья (публикация). Авторы из прошлой задачи могут
# писать статьи. У статьи может быть только один автор. У статьи должны быть
# следующие обязательные поля:
# ○ заголовок статьи с максимальной длиной 200 символов
# ○ содержание статьи
# ○ дата публикации статьи
# ○ автор статьи с удалением связанных объектов при удалении автора
# ○ категория статьи с максимальной длиной 100 символов
# ○ количество просмотров статьи со значением по умолчанию 0
# ○ флаг, указывающий, опубликована ли статья со значением по умолчанию False

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Title is {self.title}'

    def add_view(self):
        self.views += 1


# Задание 6: Создайте модель Комментарий.
# Авторы могут добавлять комментарии к своим и чужим статьям. Т.е. у комментария может быть один автор.
# И комментарий относится к одной статье. У модели должны быть следующие поля
# ○ автор
# ○ статья
# ○ комментарий
# ○ дата создания
# ○ дата изменения


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField("Комментарий")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата изменения", auto_now=True)

    def __str__(self):
        return f'Комментарий от {self.author.full_name()} на статью "{self.article.title}"'


# Задание 8
# Делаем простейшую модель магазина..Создай три модели Django: клиент, товар и заказ. Клиент
# может иметь несколько заказов. Заказ может содержатьнесколько товаров. Товар может входить в несколько заказов.
# Поля модели "Клиент":
# ○ имя клиента
# ○ электронная почта клиента
# ○ номер телефона клиента
# ○ адрес клиента
# ○ дата регистрации клиента
# Поля модели "Товар":
# ○ название товара
# ○ описание товара
# ○ цена товара
# ○ количество товара
# ○ дата добавления товара
# Поля модели "Заказ":
# ○ связь с моделью "Клиент", указывает на клиента,
# сделавшего заказ
# ○ связь с моделью "Товар", указывает на товары,
# входящие в заказ
# ○ общая сумма заказа
# ○ дата оформления заказа
#
# Допиши функции CRUD для работы с моделями Что по твоему мнению актуально в такой базе данных.

# class Client(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15)
#     address = models.TextField()
#     registration_date = models.DateField(default=timezone.now)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField()
#     added_date = models.DateField(default=timezone.now)
#
#     def __str__(self):
#         return self.title
#
#
# class Order(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
#     products = models.ManyToManyField(Product, related_name='orders')
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     order_date = models.DateField(default=timezone.now)
#
#     def __str__(self):
#         return f'Order {self.id} by {self.client.name}'
