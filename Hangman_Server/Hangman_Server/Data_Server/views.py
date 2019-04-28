from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Achievement, Match, Game_Data
from .serializers import user_Serializer, achievement_Serializer, match_Serializer, game_Serializer
from django.http import HttpResponse, HttpResponseNotFound
from .randWordGen import gen


class user_View(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_Serializer

class achievement_View(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = achievement_Serializer

class match_View(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = match_Serializer

class game_View(viewsets.ModelViewSet):
    queryset = Game_Data.objects.all()
    serializer_class = game_Serializer 

def post_Words(request):
    Game_Data_instance = Game_Data.objects.create(gameID = '1')
    word = gen(1)
    return HttpResponse(word)
