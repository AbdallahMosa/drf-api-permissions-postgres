from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import GameSerializer,MovieSerializer
from .permissions import isOwnerOrReadOnly
from .models import Game,Movie
from rest_framework import permissions
# Create your views here.
class GameListView(ListCreateAPIView):
    queryset=Game.objects.all()
    serializer_class= GameSerializer
    permission_classes = [permissions.IsAuthenticated]
class GameDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Game.objects.all()
    serializer_class= GameSerializer
    permission_classes = [isOwnerOrReadOnly]
class MovieListView(ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class= MovieSerializer
    permission_classes = [permissions.AllowAny]
class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class= MovieSerializer
    permission_classes = [isOwnerOrReadOnly]