from django.core.management.base import BaseCommand
from s02app.models import Article


class Command(BaseCommand):
    help = "Удаляет статью по ID"

    def add_arguments(self, parser):
        parser.add_argument('article_id', type=int, help='ID статьи')

    def handle(self, *args, **kwargs):
        article_id = kwargs['article_id']
        try:
            article = Article.objects.get(id=article_id)
            article.delete()
            self.stdout.write(self.style.SUCCESS(f"Статья с ID {article_id} успешно удалена."))
        except Article.DoesNotExist:
            self.stdout.write(self.style.ERROR("Статья с указанным ID не найдена."))

# python manage.py delete_article <article_id>
