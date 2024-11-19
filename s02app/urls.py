from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('game1/', views.game1, name='game1'),
    path('game2/', views.game2, name='game2'),
    path('game3/', views.game3, name='game3'),
    path('main/', views.main, name='main'),
    path('my/', views.my, name='my'),
    path('coin/', views.coin_flip, name='coin'),
    # Семинар 3
    path('s301_my/', views.s301_my, name='s301_my'),
    path('s301_about/', views.s301_about, name='s301_about'),
    path('s303_game1/<int:flips>', views.s303_game1, name='s301_game1'),
    path('s303_game2/<int:flips>', views.s303_game2, name='s301_game2'),
    path('s303_game3/<int:flips>', views.s303_game3, name='s301_game3'),
    path('s304_article/<int:id_author>', views.s304_article, name='s304_article'),
    path('s305_full_article/<int:id_article>', views.s305_full_article, name='s305_full_article'),
    # Семинар 4
    path('perform_action/', views.perform_action, name='perform_action'),
    path('s403_author/', views.s403_author, name='s403_author'),
    path('s404_article/', views.s404_article, name='s404_article'),



]