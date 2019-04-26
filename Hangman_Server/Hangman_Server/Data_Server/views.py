from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import user_Serializer

class user_View(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_Serializer


