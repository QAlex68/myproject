# Работа с данными в моделях - Создание объектов модели, create
# Для создания нового объекта модели необходимо создать экземпляр класса модели и заполнить его поля значениями.
# Например, чтобы создать нового пользователя, мы можем использовать следующий код в файле
# myapp2/management/commands/make_products.py:


from django.core.management.base import BaseCommand
from s02app.models import Article, Author


# class Command(BaseCommand):
#     help = "Create Article."
#
#     # title = models.CharField(max_length=200)
#     # text = models.TextField()
#     # publication_date = models.DateField(auto_now_add=True)
#     # author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     # category = models.CharField(max_length=100)
#     # views = models.PositiveIntegerField(default=0)
#     # is_published = models.BooleanField(default=False)
#
#     def handle(self, *args, **kwargs):
#         article = Article(title='Про елки',
#                           text='В лесу родилась елочка!',
#                           author=Author.objects.filter(pk=1).first(),
#                           category='Про деревья'
#                           )
#         article.save()
#         self.stdout.write(f'Статья: {article} добавлена!')

class Command(BaseCommand):
    help = "Создает новую статью"

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Заголовок статьи')
        parser.add_argument('text', type=str, help='Текст статьи')
        parser.add_argument('author', type=int, help='ID автора')
        parser.add_argument('category', type=str, help='Категория статьи')

    def handle(self, *args, **kwargs):
        title = kwargs['title']
        text = kwargs['text']
        author = kwargs['author']
        category = kwargs['category']

        try:
            author = Author.objects.get(pk=author)
            article = Article.objects.create(
                title=title,
                text=text,
                author=author,
                category=category,
                # is_published=True
            )
            self.stdout.write(self.style.SUCCESS(f"Статья '{article.title}' успешно создана."))
        except Author.DoesNotExist:
            self.stdout.write(self.style.ERROR("Автор с указанным ID не найден."))

# python manage.py creat_article "Заголовок 1" "Текст статьи 1" 1 "Категория 1"  Двойные кавычки критично! с одинарными может не сработать
# python manage.py creat_article "Заголовок 2" "Текст статьи 2" 1 "Категория 2"
