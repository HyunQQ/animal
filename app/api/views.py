from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import AnimalUser
from app.api.serializers import UserSerializer, AnimalUserSerializer
from app.api.animal_api import get_sido, get_kind, get_shelter, get_sigungu, get_abandonment

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


class AnimalUserViewSet(viewsets.ModelViewSet):
    queryset = AnimalUser.objects.all().order_by('-created_at')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnimalUserSerializer

class SidoList(APIView):
    def get(self, request):
        rslt = get_sido()
        return Response(rslt)

class SiGunGuList(APIView):
    def get(self, request):
        sido_code = request.query_params.get('upr_cd')

        if sido_code is None:
            content = {'please check sido': 'need to input upr_cd information'}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            rslt = get_sigungu(sido_code)
            return Response(rslt)


class ShelterList(APIView):
    def get(self, request):
        upr_cd = request.query_params.get('upr_cd')
        org_cd = request.query_params.get('org_cd')

        if upr_cd is None:
            content = {'Check sido information': 'Need to input upr_cd information'}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        elif org_cd is None:
            content = {'Check sigungu information': 'Need to input org_cd information'}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            rslt = get_shelter(upr_cd, org_cd)
            return Response(rslt)


class KindList(APIView):
    def get(self, request):
        up_kind_cd = request.query_params.get('up_kind_cd')

        if up_kind_cd is None:
            content = {'Check kind information': 'Need to input up_kind_cd information'}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            rslt = get_kind(up_kind_cd)
            return Response(rslt)


class AbandonmentList(APIView):
    def get(self, request):
        up_kind_cd = request.query_params.get('up_kind_cd')
        test = request.parsers
        print(test)
        # myDict = dict(queryDict.iterlists())


        if up_kind_cd is None:
            content = {'Check kind information': 'Need to input up_kind_cd information'}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            rslt = get_abandonment(up_kind_cd)
            return Response(rslt)