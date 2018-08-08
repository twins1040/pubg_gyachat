from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('players/<shard>/<playerName>/', views.searchPlayer, name='searchPlayer')
]
