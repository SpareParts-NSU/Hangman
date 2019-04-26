from rest_framework import serializers
from .models import User

class user_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'alias', 'email', 'password')

