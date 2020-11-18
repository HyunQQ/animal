import logging
from pprint import pformat
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
# from rest_framework.views import APIView

from app.models import AnimalUser
from app.api.serializers import UserSerializer, AnimalUserSerializer
from app.api.animal_api import get_sido, get_kind, get_shelter, get_sigungu, get_abandonment
from app.api.shelter_api import get_shelter_detail
from app.common.common import get_querys
from app.common.decorator import param_validator
from app.common.result import ok, error


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


# FBV
@api_view(['GET'])
@param_validator
def sido(request):
    querys = get_querys(request)
    rslt = get_sido(querys)
    if not isinstance(rslt['rslt'], list):
        logging.error(pformat(rslt['rslt']))
        return error(rslt, msg="Open API Server Error")

    return ok(rslt)


@api_view(['GET'])
@param_validator
def sigungu(request):
    querys = get_querys(request)
    rslt = get_sigungu(querys)
    if not isinstance(rslt['rslt'], list):
        logging.error(pformat(rslt['rslt']))
        return error(rslt, msg="Open API Server Error")

    return ok(rslt)


@api_view(['GET'])
@param_validator
def shelter(request):
    querys = get_querys(request)
    rslt = get_shelter(querys)
    if not isinstance(rslt['rslt'], list):
        logging.error(pformat(rslt['rslt']))
        return error(rslt, msg="Open API Server Error")

    return ok(rslt)


@api_view(['GET'])
@param_validator
def shelter_detail(request):
    querys = get_querys(request)
    rslt = get_shelter_detail(querys)
    if not isinstance(rslt['rslt'], list):
        logging.error(pformat(rslt['rslt']))
        return error(rslt, msg="Open API Server Error")

    return ok(rslt)


@api_view(['GET'])
@param_validator
def kind(request):
    querys = get_querys(request)
    rslt = get_kind(querys)
    if not isinstance(rslt['rslt'], list):
        logging.error(pformat(rslt['rslt']))
        return error(rslt, msg="Open API Server Error")

    return ok(rslt)


@api_view(['GET'])
@param_validator
def abandonment(request):
    querys = get_querys(request)
    rslt = get_abandonment(querys)
    if not isinstance(rslt['rslt'], list):
        logging.error(pformat(rslt['rslt']))
        return error(rslt, msg="Open API Server Error")

    return ok(rslt)
