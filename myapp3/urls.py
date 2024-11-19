from django.urls import path
from .views import hello, HelloView
from .views import year_post, MonthPost, post_detail, my_view, TemplIf, view_for, index, about, post_full, author_posts

urlpatterns = [
    # path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('game1/', views.game1, name='game1'),
    # path('game2/', views.game2, name='game2'),
    # path('game3/', views.game3, name='game3'),
    # path('main/', views.main, name='main'),
    # path('my/', views.my, name='my'),
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    # Передача параметров - Преобразования пути
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    path('', my_view, name='index'),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='templ_for'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('author/<int:author_id>/', author_posts, name='author_post'),
    path('post/<int:post_id>/', post_full, name='post_full'),


]

'''
Преобразование пути в типы Python
В Django преобразование путей осуществляется с помощью приставок, которые определяют тип данных, который будет
передаваться в качестве параметра в представление. Для этого мы заключаем параметр в треугольные скобки и указываем
приставку, а далее после двоеточия слитно пишем имя параметра.
● str — приставка для передачи строки любых символов, кроме слэша.
Например, если мы хотим передать в представление информацию о конкретном посте блога, то мы можем использовать такой
путь: path('posts/<str:slug>/', post_detail). Здесь slug - это строка символов, которая является уникальным
идентификатором поста.
● int — приставка для передачи целого числа. Например, если мы хотим передать в представление информацию о конкретном 
пользователе по его идентификатору, то мы можем использовать такой путь:
path('users/<int:id>/', user_detail). Здесь id - это целое число, которое является уникальным идентификатором 
пользователя.
● slug — приставка для передачи строки, содержащей только буквы, цифры, дефисы и знаки подчеркивания. Например, если мы
хотим передать в представление информацию о конкретной категории товаров, то мы можем использовать такой путь:
path('categories/<slug:slug>/', category_detail). Здесь slug - это строка символов, которая является уникальным 
идентификатором категории.
● uuid — приставка для передачи уникального идентификатора. Например, если мы хотим передать в представление информацию
о конкретном заказе, то мы можем использовать такой путь: path('orders/<uuid:pk>/', order_detail). 
Здесь pk - это уникальный идентификатор заказа.
● path — приставка для передачи строки любых символов, включая слэши. Например, если мы хотим передать в представление 
информацию о конкретном файле на сервере, то мы можем использовать такой путь:
path('files/<path:url>/', file_detail). Здесь url - это строка символов, которая содержит путь к файлу на сервере.
'''