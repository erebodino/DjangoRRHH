from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class AreaModel(models.Model):
    area = models.CharField(max_length=30, blank=False, null=False)
    rotativo = models.BooleanField(default=False)

    def __str__(self):
        return self.area

class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    dni = models.IntegerField(unique=True,null=False,blank=True)
    area = models.ForeignKey(AreaModel, on_delete=models.CASCADE)
    legajo = models.IntegerField(unique=True,null=False,blank=True)
    fecha_ingreso = models.DateField(null=False,blank=True)
    foto = models.ImageField(upload_to='users/%Y/%m/%d/',
                              null=False,blank=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    
    dni = models.IntegerField(unique=True,null=False,blank=True)
    area = models.ForeignKey(AreaModel, on_delete=models.CASCADE)
    legajo = models.IntegerField(unique=True,null=False,blank=True)
    fecha_ingreso = models.DateField(null=False,blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

# Create your models here.
