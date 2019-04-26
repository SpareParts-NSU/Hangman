from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Achievement
from .serializers import user_Serializer, achievement_Serializer

class user_View(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_Serializer

class achievement_View(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = achievement_Serializer

