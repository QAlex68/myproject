from django.core.management.base import BaseCommand
from s02app.models import Article, Author, Comment

class Command(BaseCommand):
    help = "Создать комментарий."

    def handle(self, *args, **kwargs):
        author = Author.objects.get(pk=1)  # Замените на нужный ID автора
        article = Article.objects.get(pk=1)  # Замените на нужный ID статьи

        # Создание комментария
        comment = Comment.objects.create(
            author=author,
            article=article,
            text="Отличная статья!"
        )

        # Вывод подтверждения
        self.stdout.write(f'Комментарий к статье ID-{article.id} от автора ID-{author.id} добавлен!')
