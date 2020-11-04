from app.models import AnimalUser
from rest_framework import viewsets, permissions
from .serializers import AnimalUserSerializer

class AnimalUserViewSet(viewsets.ModelViewSet):
    queryset = AnimalUser.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnimalUserSerializer