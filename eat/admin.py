from django.contrib import admin
from .models import *

# Register your models here.
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

admin.site.register(Menu)
admin.site.register(Order)