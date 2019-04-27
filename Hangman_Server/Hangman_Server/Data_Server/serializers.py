from rest_framework import serializers
from .models import User, Achievement, Match

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
        fields = ('Player_1', 'Player_2', 'level', 'seed', 'Winner')


