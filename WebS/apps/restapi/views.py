from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from .models import ChessGame
from .serializers import ChessGameSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def chess_games_list(request):

    """get all games and serialize
            return JSON"""
    if request == 'GET':
        chess_game = ChessGame.objects.all()
        serializer = ChessGameSerializer(chess_game, many=True)
        return JsonResponse({'chess_games':serializer.data})
    if request == 'POST':
        serializer = ChessGameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)