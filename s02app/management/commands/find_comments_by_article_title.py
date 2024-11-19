# Задание 7 Поиск всех комментариев по названию статьи
# Код работает неверно сначала нужно найти ид автора по имени в таблице автор

from django.core.management.base import BaseCommand
from s02app.models import Comment


class Command(BaseCommand):
    help = "Найти все комментарии по названию статьи."

    def add_arguments(self, parser):
        parser.add_argument('article_title', type=str, help='Название статьи')
        parser.add_argument('--order_by', type=str, default='-created_at', help='Поле для сортировки')
        parser.add_argument('--limit', type=int, default=10, help='Количество возвращаемых комментариев')

    def handle(self, *args, **kwargs):
        article_title = kwargs['article_title']
        order_by = kwargs['order_by']
        limit = kwargs['limit']

        comments = Comment.objects.filter(article__title=article_title).order_by(order_by)[:limit]

        if comments:
            for comment in comments:
                self.stdout.write(f'Комментарий: {comment.text} (ID: {comment.id})')
        else:
            self.stdout.write('Комментарии не найдены.')


# python manage.py find_comments_by_article_title "Как стать разработчиком" --order_by="created_at" --limit=5