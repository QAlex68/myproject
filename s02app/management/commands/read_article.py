from django.core.management.base import BaseCommand
from lss02app.mode import Article


class Command(BaseCommand):
    help = "Показать статью по ID"

    def add_arguments(self, parser):
        parser.add_argument('article_id', type=int, help='ID статьи')

    def handle(self, *args, **kwargs):
        article_id = kwargs['article_id']
        try:
            article = Article.objects.get(id=article_id)
            self.stdout.write(
                self.style.SUCCESS(f"Статья: {article.title}\nТекст: {article.text}\nПросмотры: {article.views}"))
        except Article.DoesNotExist:
            self.stdout.write(self.style.ERROR("Статья с указанным ID не найдена."))

# python manage.py read_article <article_id>
