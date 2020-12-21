from django.contrib.auth.models import User
from rest_framework import serializers
from app.models.users import AnimalUser
from app.models.locations import Sido, Sigungu
from app.models.animal import KindCd


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id', 'username', 'email')
        fields = '__all__'


class AnimalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalUser
        fields = '__all__'


class SidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sido
        fields = '__all__'


class SigunguSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sigungu
        fields = ('sigunguCd', 'sigunguNm')


class KindCdSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindCd
        fields = '__all__'