from rest_framework import serializers
from .models import User, Achievement

class user_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar', 'alias', 'email', 'password')

class achievement_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'alias')

