from django.contrib.auth.models import User
from rest_framework import serializers
from app.models.users import AnimalUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id', 'username', 'email')
        fields = '__all__'


class AnimalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalUser
        fields = '__all__'