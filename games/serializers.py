from rest_framework import serializers
from .models import Game,Movie
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model= Game
        fields='__all__'
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movie
        fields='__all__'