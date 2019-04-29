from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Achievement, Match, Game_Data, Leader_Board
from .serializers import user_Serializer, achievement_Serializer, match_Serializer, game_Serializer, leaderboard_Serializer
from django.http import HttpResponse, HttpResponseNotFound
from .randWordGen import gen

count = 0

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

class leaderboard_View(viewsets.ModelViewSet):
    queryset = Leader_Board.objects.all()
    serializer_class = leaderboard_Serializer


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_match_id(request):
    global count
    print (get_client_ip(request))
    global Game_Data_instance
    if (count == 0):
        word = gen(1)
        Game_Data_instance = Game_Data.objects.create(word = word, p1_ip = get_client_ip(request))
        count += 1
        return HttpResponse(Game_Data_instance.id)
    else :
        Game_Data.objects.update(p2_ip = get_client_ip(request), gameStart = True)
        count = 0
        return HttpResponse(Game_Data_instance.id)

def get_word(request):
    word = gen(1)
    Game_Data_instance = Game_Data.objects.create(word = word)
    return HttpResponse(word)





