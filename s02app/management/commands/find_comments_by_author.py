# Задание 7 Поиск всех комментариев автора по имени

from django.core.management.base import BaseCommand
from s02app.models import Comment


class Command(BaseCommand):
    help = "Найти все комментарии автора по имени."

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str, help='Имя автора комментария')
        parser.add_argument('last_name', type=str, help='Фамилия автора комментария')
        parser.add_argument('--order_by', type=str, default='-created_at', help='Поле для сортировки')
        parser.add_argument('--limit', type=int, default=10, help='Количество возвращаемых комментариев')

    def handle(self, *args, **kwargs):
        first_name = kwargs['first_name']
        last_name = kwargs['last_name']
        order_by = kwargs['order_by']
        limit = kwargs['limit']

        comments = Comment.objects.filter(author__name=first_name, author__last_name=last_name).order_by(order_by)[
                   :limit]

        if comments:
            for comment in comments:
                self.stdout.write(f'Комментарий: {comment.text} (ID: {comment.id})')
        else:
            self.stdout.write('Комментарии не найдены.')

# python manage.py find_comments_by_author "Иван" "Иванов" --order_by="created_at" --limit=5

