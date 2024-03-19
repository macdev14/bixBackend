from rest_framework import viewsets

from apps.api.serializers import CompanySerializer, CustomTokenSerializer, EmployeeSerializer, UserSerializer
from apps.authentication.models import Company, Employee, User
# Create your views here.
# ViewSets define the view behavior.
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)


from django.contrib.auth import get_user_model

class ApiCompanyAddon(viewsets.ModelViewSet): 
    pass

class UserViewSet(ApiCompanyAddon):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        if self.request.user.is_anonymous:
            return User.objects.filter()
        else:
            return User.objects.filter(company=self.company).order_by('username')

    
class CompanyViewSet(ApiCompanyAddon):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Company.objects.filter()

class EmployeeViewSet(ApiCompanyAddon):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Employee.objects.filter()
        
        return Employee.objects.filter().order_by('name')




class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

