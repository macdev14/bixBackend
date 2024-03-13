from rest_framework import routers, serializers, viewsets
from apps.authentication.models import Company, Employee, User
from django.utils.translation import gettext_lazy as _
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'cnpj', 'name')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    company_name = serializers.ReadOnlyField(source='company.name')
    class Meta:
        model = Employee
        fields = ('id', 'cpf', 'name', 'company', 'company_name')