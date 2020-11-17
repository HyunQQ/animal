from django.urls import path, include
from rest_framework import routers
from app.api.views import UserViewSet, AnimalUserViewSet
from app.api.views import sido, sigungu, shelter, shelter_detail, kind, abandonment

app_name='app'


router = routers.DefaultRouter()
router.register(r'basicusers', UserViewSet)
router.register(r'animaluser', AnimalUserViewSet)

# user_list = UserView.as_view({
#     'get' :'list'
# })

urlpatterns=[
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('get_sido/', SidoList.as_view()),
    # path('get_sigungu/', SiGunGuList.as_view()),
    # path('get_shelter/', ShelterList.as_view()),
    # path('get_kind/', KindList.as_view()),
    # path('get_abandonment/', AbandonmentList.as_view()),
    # path('get_shelter_detail/', ShelterDetail.as_view()),

    # path('test/', test_api),
    path('sido/', sido),
    path('sigungu/', sigungu),
    path('shelter/', shelter),
    path('shelter_detail/', shelter_detail),
    path('kind/', kind),
    path('abandonment/', abandonment)
]

