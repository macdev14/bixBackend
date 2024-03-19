from django.urls import include, path
from rest_framework import routers


from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authtoken.views import(
    obtain_auth_token
)
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename="users")
router.register(r'company', views.CompanyViewSet , basename="company")
router.register(r'employees', views.EmployeeViewSet , basename="employee")
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]