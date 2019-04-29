from rest_framework import serializers
from .models import User, Achievement, Match, Game_Data, Leader_Board

class user_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar', 'alias', 'email', 'password')

class achievement_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('player', 'experience', 'points', 'achievement')

class match_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'Player_1', 'Player_2', 'level', 'seed', 'Winner')

class game_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Data
        fields = ('id', 'hit_p1', 'hit_p2', 'word', 'gameStart', 'Winner')

class leaderboard_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Leader_Board
        fields = ('id', 'player', 'achievement')