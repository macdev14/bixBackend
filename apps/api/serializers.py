import json
from django.core import serializers as core_serializers
from rest_framework import routers, serializers, viewsets
from apps.authentication.models import Company, Employee, User
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superuser']

class CustomTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user_serializer = UserSerializer(instance=self.user)
        serialized_user = user_serializer.data
        data['user'] = serialized_user
        print(data)
        return data
    
    
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'cnpj', 'name')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    company_name = serializers.ReadOnlyField(source='company.name')
    class Meta:
        model = Employee
        fields = ('id', 'cpf', 'name', 'company', 'company_name', 'entered_at', 'exited_at', 'vacation_days')