from rest_framework import serializers
from .models import ChessGame

class ChessGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessGame
        fields = ['id', 'player_name_white', 'player_name_black', 'moves', 'date', 'winner']