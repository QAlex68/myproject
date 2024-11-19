# yourapp/management/commands/update_article.py
from django.core.management.base import BaseCommand
from s02app.models import Article


class Command(BaseCommand):
    help = "Обновляет статью по ID"

    def add_arguments(self, parser):
        parser.add_argument('article_id', type=int, help='ID статьи')
        parser.add_argument('--title', type=str, help='Новый заголовок')
        parser.add_argument('--text', type=str, help='Новый текст')
        parser.add_argument('--is_published', type=bool, help='Статус публикации (True или False)')

    def handle(self, *args, **kwargs):
        article_id = kwargs['article_id']
        title = kwargs.get('title')
        text = kwargs.get('text')
        is_published = kwargs.get('is_published')

        try:
            article = Article.objects.get(id=article_id)
            if title:
                article.title = title
            if text:
                article.text = text
            if is_published is not None:
                article.is_published = is_published

            article.save()
            self.stdout.write(self.style.SUCCESS(f"Статья '{article.title}' успешно обновлена."))
        except Article.DoesNotExist:
            self.stdout.write(self.style.ERROR("Статья с указанным ID не найдена."))

# python manage.py update_article 2 --title "Про сосну" --text "В лесу сосна родилась" --is_published True
