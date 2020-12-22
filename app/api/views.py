import logging
from pprint import pformat
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
# from rest_framework.views import APIView

# from app.models import AnimalUser
from app.api.serializers import UserSerializer, AnimalUserSerializer, SidoSerializer, SigunguSerializer, KindCdSerializer
from app.api.animal_api import get_sido, get_kind, get_shelter, get_sigungu, get_abandonment
from app.api.shelter_api import get_shelter_detail
from app.api.addon_api import get_shelter_nearby
from app.common.common import get_querys
from app.common.decorator import param_validator
from app.common.result import ok, error, make_response_content
from app.models.locations import Sido, Sigungu
from app.models.animal import KindCd
from app.common.set_default_db import set_kind_info, set_sido_info


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
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
    User = get_user_model()
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnimalUserSerializer


# Defalut Value Set
@api_view(['POST'])
@param_validator
def set_default_db(request):
    if Sido.objects.all().count() == 0:
        set_sido_info()

    if KindCd.objects.all().count() == 0:
        set_kind_info()

    return ok('Default Value Set')

# FBV
@api_view(['GET'])
@param_validator
def sido(request):
    try:
        sido = Sido.objects.all()
    except Sido.DoesNotExist:
        return error("", msg="Sido data does not exist.")

    serializer = SidoSerializer(sido, many=True)
    rslt = make_response_content(response_data=serializer.data, req_param={}, info_data={})

    return ok(rslt)

# sido old version
# @api_view(['GET'])
# @param_validator
# def sido(request):
#     querys = get_querys(request)
#     querys['numOfRows'] = '20'  # 한번에 sido 값을 모두 가져오기 위해 설정(10개일 경우 잘림)
#     rslt = get_sido(querys)
#     if not isinstance(rslt['rslt'], list):
#         logging.error(pformat(rslt['rslt']))
#         return error(rslt, msg="Open API Server Error")
#
#     return ok(rslt)


@api_view(['GET'])
@param_validator
def sigungu(request):
    querys = get_querys(request)
    try:
        sigungu = Sigungu.objects.filter(sidoCd=querys['upr_cd'])
    except Sigungu.DoesNotExist:
        return error("", msg="Sido data does not exist.")

    serializer = SigunguSerializer(sigungu, many=True)
    rslt = make_response_content(response_data=serializer.data, req_param=querys, info_data={})

    return ok(rslt)

# sigungu old version
# @api_view(['GET'])
# @param_validator
# def sigungu(request):
#     querys = get_querys(request)
#     rslt = get_sigungu(querys)
#     if not isinstance(rslt['rslt'], list):
#         logging.error(pformat(rslt['rslt']))
#         return error(rslt, msg="Open API Server Error")
#
#     return ok(rslt)


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
def shelter_nearby(request):
    querys = get_querys(request)
    rslt = get_shelter_nearby(querys)
    if not isinstance(rslt['rslt'], list):
        logging.error(pformat(rslt['rslt']))
        return error(rslt, msg="Open API Server Error")

    return ok(rslt)


@api_view(['GET'])
@param_validator
def kind_cd(request):
    try:
        kind_cd = KindCd.objects.all()
    except KindCd.DoesNotExist:
        return error("", msg="Sido data does not exist.")

    serializer = KindCdSerializer(kind_cd, many=True)
    rslt = make_response_content(response_data=serializer.data, req_param={}, info_data={})

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



