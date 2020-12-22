from django.urls import path, include
from rest_framework import routers
from app.api.views import UserViewSet, AnimalUserViewSet
from app.api.views import sido, sigungu
from app.api.views import shelter, shelter_detail, shelter_nearby
from app.api.views import kind, kind_cd, abandonment, set_default_db

app_name='app'

router = routers.DefaultRouter()
router.register(r'basicusers', UserViewSet)
router.register(r'animaluser', AnimalUserViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('set_default/', set_default_db),
    path('sido/', sido),
    path('sigungu/', sigungu),
    path('shelter/', shelter),
    path('shelter_detail/', shelter_detail),
    path('shelter_nearby/', shelter_nearby),
    path('kind_cd/', kind_cd),
    path('kind/', kind),
    path('abandonment/', abandonment)
]
