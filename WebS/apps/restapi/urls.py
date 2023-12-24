from django.urls import path
from . import views

urlpatterns = [
path('chess_games/', views.chess_games_list)
]

