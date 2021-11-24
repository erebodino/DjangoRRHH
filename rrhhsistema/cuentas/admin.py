from django.contrib import admin
from django.db.models import fields
from .models import AreaModel, Profile
from django.contrib.auth.admin import UserAdmin

@admin.register(AreaModel)
class AreaModelAdmin(admin.ModelAdmin):
    fields = ('area','rotativo')

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    fields = ('dni','area','legajo','fecha_ingreso')


# Register your models here.
