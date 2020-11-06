from django.urls import path, include
from rest_framework import routers
from app.api.views import UserViewSet, AnimalUserViewSet, SidoList

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
    # path('users/', user_list, name='user_list')
    path('get_sido/', SidoList.as_view())

]

