from rest_framework import viewsets

from apps.api.serializers import CompanySerializer, EmployeeSerializer, UserSerializer
from apps.authentication.models import Company, Employee, User
# Create your views here.
# ViewSets define the view behavior.

class ApiCompanyAddon(viewsets.ModelViewSet): 
    pass
class UserViewSet(ApiCompanyAddon):
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return User.objects.filter()
        else:
            return User.objects.filter(company=self.company).order_by('username')

    
class CompanyViewSet(ApiCompanyAddon):
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.filter()

class EmployeeViewSet(ApiCompanyAddon):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Employee.objects.filter()
        
        return Employee.objects.filter().order_by('name')

    
