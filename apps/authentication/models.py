

# Create your models here.





# from asyncio.streams import _ClientConnectedCallback
from django.dispatch import receiver
from django.apps import apps
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.br.models import BRCPFField, BRCNPJField
import datetime

from rest_framework.authtoken.models import Token
from django.contrib.auth.signals import user_logged_in

# Create your models here.

class Company(models.Model):
    # user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)
    cnpj = BRCNPJField(_('Business Document Number'), unique=True)
    name = models.CharField(_('Business Name'), max_length=512)
    
    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {"name": self.name, "cnpj": self.cnpj}
    
    def to_json(self):
        return {"name": self.name, "cnpj": self.cnpj}

    class Meta:
        verbose_name_plural = _("Companies")
        verbose_name = _("Company")

class Employee(models.Model):
    # user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(_('Employee Name'), max_length=512)
    cpf = BRCPFField(_('Document Number'), unique=True) 
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)

    def get_company(self):
        try:
            return self.company
        except Exception as e:
            print(e)
            return    
  

    
class User(AbstractUser):
    pass
    # is_employee = models.BooleanField(_('Employee Status'), help_text=_('Designates whether the user can log in as an employee.'), default=False)
    # is_company = models.BooleanField(_('Company Status'), help_text=_('Designates whether the user can log in as a staff member.') , default=False)

    # def get_company(self):
    #     try:
    #         if self.is_employee:
    #             if Employee.objects.filter(user__pk=self.pk).exists():
    #                 e = Employee.objects.get(user__pk=self.pk)
    #                 return e.company
    #         elif self.is_company:
    #             if Company.objects.filter(user__pk=self.pk).exists():
    #                 c = Company.objects.get(user__pk=self.pk)    
    #                 return c
            
    #     except Exception as e:
    #         print(e)
    #         return
   
    # def get_company_email(self):
    #     c = self.get_company().user.email
    #     return c
   
    
@receiver(user_logged_in, sender=User)
def create_auth_token(sender, user, request, **kwargs):
    print(user)
    if Token.objects.filter(user=user).exists(): 
        Token.objects.get(user=user).delete()
    Token.objects.create(user=user)
    print('logged in user')

user_logged_in.connect(create_auth_token) 