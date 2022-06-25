#from collections import UserString
#from django.urls import url, path
from django.urls import  path
from . import views
#from api.api.core import views
from User.api.views import  ApiUserRegister, authenticate_user, project_list
from rest_framework_simplejwt import views as jwt_views  



urlpatterns = [
    path('', views.getRoutes),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/validate/', views.TokenValidate.as_view(), name='token_validate'),
    path('authenticate_user/<token>/', authenticate_user, name='authenticate_users'),
    path('ApiUserRegister/<company>/<username>/', ApiUserRegister, name='ApiUserRegister'),
    path('project_list/', project_list, name='project_list')
 ]
