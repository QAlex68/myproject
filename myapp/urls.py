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

]
