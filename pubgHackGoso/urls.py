from django.urls import path

from . import views

app_name = 'pubg_gyachat'
urlpatterns = [
    path('', views.index, name='index'),
    path('players/<player_id>/', views.closet, name='closet'),
    path('players/<player_id>/gyachat/', views.gyachat, name='gyachat'),
    path('players/<player_id>/gyachat/upcount/', views.upcount, name='upcount'),
    path('players/<player_id>/gyachat/shoot/', views.shoot, name='shoot'),
    path('search/', views.search_player, name='search'),
]
