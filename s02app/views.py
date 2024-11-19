import logging
import random
from typing import Any

from django.db.models.manager import BaseManager
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from s02app.models import CoinFlip, Author, Article
from .forms import RandomForm, AuthorForm, ArticleForm

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def about(request):
    try:
        # some code that might raise an exception
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse("This is the about page.")


def game1(request):
    result = random.choice(['Орел', 'Решка'])
    logger.info('Game1 page accessed')
    return HttpResponse(f'<h1>Игра орел решка!</h1><br>Выпало: {result}')


def game2(request):
    result = random.randint(0, 100)
    logger.info('Game2 page accessed')
    return HttpResponse(f'<h1>Игра случайное число от 1 до 100!</h1><br>Выпало: {result}')


def game3(request):
    logger.info('Game3 page accessed')
    result = random.randint(1, 6)
    return HttpResponse(f'<h1>Игра бросание кубика!</h1><br>Выпало: {result}')


def main(request):
    logger.info('Main page accessed')
    html = '''<h1>Главная страница</h1><br><p> Текст на главной странице</p>'''
    return HttpResponse(html)


def my(request):
    logger.info('My page accessed')
    html = '''<h1>Моя страница</h1><br><p> Текст на моей странице</p>'''
    return HttpResponse(html)


# Задание №1
# Создайте модель для запоминания бросков монеты: орёл или
# решка.
# Также запоминайте время броска

# def coin_flip(request):
#     # result = random.choice(['heads', 'tails'])
#     flips = CoinFlip.objects.all()
#     return HttpResponse(f'flips: {flips}')

# Сем 2 задание 2

def coin_flip(request):
    # result = random.choice(['heads', 'tails'])
    flips = CoinFlip.get_last_flips(3)
    return HttpResponse(f'flips: {flips}')


# Семинар 3-1-2
def s301_my(request):
    logger.info('Main page accessed')
    context: dict[str, str] = {
        'title': 'Главная страница',
        'content': "<h1>Задачи 1-2 семинара 3!</h1><br>"
                   "1. Изменяем задачу 8 из семинара 1 с выводом двух html страниц: главной и о себе.<br>"
                   "Перенесите вёрстку в шаблоны. Представления должны пробрасывать полезную информацию<br>"
                   "в шаблон через контекст.<br>"
                   "2. Выделите общий код шаблонов и создайте родительский шаблон 301_base.html.<br>"
                   " Внесите правки в дочерние шаблоны.<br>"
                   "http://127.0.0.1:8000/sem/s301_my/ , http://127.0.0.1:8000/sem/s301_about/",
    }
    return render(request, 's02app/301_my.html', context)


def s301_about(request):
    logger.info('My page accessed')
    context: dict[str, str] = {
        'title': 'Моя страница',
        'content': "<h1>Эта страница обо мне!</h1><br>Текст на моей странице",
    }
    return render(request, 's02app/303_my.html', context)


# Задание №3-3
# Доработаем задачу 7 из урока 1, где бросали монетку, игральную кость и генерировали случайное число.
# Маршруты могут принимать целое число - количество бросков.
# Представления создают список с результатами бросков и передают его в контекст шаблона.
# Необходимо создать универсальный шаблон для вывода результатов любого из трёх представлений.

def s303_game1(request, flips: int):
    logger.info('Game1 page accessed')
    flips_list: list[str] = [random.choice(['Орел', 'Решка']) for _ in range(flips)]
    context: dict[str, Any] = {'title': 'Игра Орел Решка', 'content': flips_list}
    return render(request, 's02app/303_game.html', context)


def s303_game2(request, flips: int):
    logger.info('Game1 page accessed')
    flips_list: list[str] = [str(random.randint(0, 100)) for _ in range(flips)]
    context: dict[str, Any] = {'title': 'Игра случайные числа', 'content': flips_list}
    return render(request, 's02app/303_game.html', context)


def s303_game3(request, flips: int):
    logger.info('Game3 page accessed')
    flips_list: list[int] = [random.randint(1, 6) for _ in range(flips)]
    context: dict[str, Any] = {'title': 'Игра бросание кубика!', 'content': flips_list}
    return render(request, 's02app/303_game.html', context)


def s304_article(request, id_author: int):
    author: Author | None = Author.objects.filter(id=id_author).first()
    arts: BaseManager[Article] = Article.objects.filter(author=author)
    context: dict[str, Any] = {
        'title': f'Статьи автора: {author.full_name()}',
        'article_list': arts
    }
    return render(request, 's02app/304_article.html', context)


def s305_full_article(request, id_article: int):
    article: Article = get_object_or_404(Article, pk=id_article)
    article.add_view()
    article.save()
    context: dict[str, Any] = {
        'title': 'Статья',
        'article': article,
    }
    return render(request, 's02app/305_full_article.html', context)


# Семинар 4-1-2
# Доработаем задачу про броски монеты, игральной кости и случайного числа.
# Создайте форму, которая предлагает выбрать: монета, кости, числа.
# Второе поле предлагает указать количество попыток от 1 до 64.
# Создайте представление, которое выводит форму выбора.
# В зависимости от переданных значений представление
# вызывает одно из трёх представлений, созданных на
# прошлом семинаре (если данные прошли проверку, конечноже).

def s401_game1(request, flips: int):
    # logger.info('Game1 page accessed')
    flips_list: list[str] = [random.choice(['Орел', 'Решка']) for _ in range(flips)]
    context: dict[str, Any] = {'title': 'Игра Орел Решка', 'content': flips_list}
    return render(request, 's02app/303_game.html', context)


def s401_game2(request, flips: int):
    # logger.info('Game3 page accessed')
    flips_list: list[int] = [random.randint(1, 6) for _ in range(flips)]
    context: dict[str, Any] = {'title': 'Игра бросание кубика!', 'content': flips_list}
    return render(request, 's02app/303_game.html', context)


def s401_game3(request, flips: int):
    # logger.info('Game1 page accessed')
    flips_list: list[str] = [str(random.randint(0, 100)) for _ in range(flips)]
    context: dict[str, Any] = {'title': 'Игра случайные числа', 'content': flips_list}
    return render(request, 's02app/303_game.html', context)


def perform_action(request):  # Работа с формой
    if request.method == 'POST':
        form = RandomForm(request.POST)
        if form.is_valid():
            event_type = form.cleaned_data['event_type']
            attempts = form.cleaned_data['attempts']
            if event_type == 'coin':
                return s401_game1(request, attempts)
            elif event_type == 'dice':
                return s401_game2(request, attempts)
            elif event_type == 'number':
                return s401_game3(request, attempts)
            # logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = RandomForm()
    return render(request, 's02app/401_game.html', {'form': form})


# Задание 3-4

def s403_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form_data: dict[str, Any] = form.cleaned_data
            Author.objects.create(
                name=form_data['name'],
                last_name=form_data['last_name'],
                email=form_data['email'],
                bio=form_data['bio'],
                birthday=form_data['birthday'],
                )
    else:
        form = AuthorForm()
    authors: BaseManager[Author] = Author.objects.all()
    context: dict[str, Any] = {'authors': authors, 'form': form}
    return render(request, 's02app/403_author.html', context)


def s404_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form_data: dict[str, Any] = form.cleaned_data
            Article.objects.create(
                title = form_data['title'],
                text = form_data['text'],
                author = form_data['author'],
                category = form_data['category'],
                is_published = form_data['is_published'],
                )
            return redirect('s404_article')
    else:
        form = ArticleForm()
    context: dict[str, Any] = {'title': 'Добавить статью', 'form': form}
    return render(request, 's02app/404_article.html', context)
