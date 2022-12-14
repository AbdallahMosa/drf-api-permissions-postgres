from django.urls import path
from .views import GameListView,GameDetailView,MovieListView,MovieDetailView
urlpatterns = [
   path('', GameListView.as_view(), name='game_list'),
   path('<int:pk>', GameDetailView.as_view(),name='game_detail'),
   path('movie/', MovieListView.as_view(), name='movie_list'),
   path('movie/<int:pk>', MovieDetailView.as_view(),name='movie_detail'),
   
]