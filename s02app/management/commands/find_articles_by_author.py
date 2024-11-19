# Задание 7 Поиск всех статей автора по имени

from django.core.management.base import BaseCommand
from s02app.models import Article


class Command(BaseCommand):
    help = "Найти все статьи автора по имени."

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str, help='Имя автора')
        parser.add_argument('last_name', type=str, help='Фамилия автора')
        parser.add_argument('--order_by', type=str, default='-publication_date', help='Поле для сортировки')
        parser.add_argument('--limit', type=int, default=10, help='Количество возвращаемых статей')

    def handle(self, *args, **kwargs):
        first_name = kwargs['first_name']
        last_name = kwargs['last_name']
        order_by = kwargs['order_by']
        limit = kwargs['limit']

        articles = Article.objects.filter(author__name=first_name, author__last_name=last_name).order_by(order_by)[
                   :limit]

        if articles:
            for article in articles:
                self.stdout.write(f'{article.title} (ID: {article.id})')
        else:
            self.stdout.write('Статьи не найдены.')

# python manage.py find_articles_by_author "Иван" "Иванов" --order_by="title" --limit=5
# python manage.py find_articles_by_author "Аарон"