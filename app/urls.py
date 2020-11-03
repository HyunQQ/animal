from django.urls import path, include
from rest_framework import routers
from app.views import UserViewSet

app_name='app'


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# user_list = UserView.as_view({
#     'get' :'list'
# })

urlpatterns=[
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('users/', user_list, name='user_list')

]

