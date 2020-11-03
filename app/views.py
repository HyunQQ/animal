from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from app.serializers import UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    #url : app/get_admin
    @action(detail=False)
    def get_admin(self, request):
        qs = self.queryset.filter(is_superuser=True)
        serializer = self.get_serializer(qs)
        return Response(serializer.data)

    #url :  app/{pk}/set_test
    #수정 필요
    @action(detail=True, methods=['patch'])
    def set_first_name(self, request, pk):
        instance = self.get_object()
        instance.first_name = request.data.first_name



# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]