import logging
import random

from django.shortcuts import render
from django.http import HttpResponse

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
    # return HttpResponse(f'<h1>Игра орел решка!</h1>')
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
