from dataclasses import fields
from rest_framework.serializers import  ModelSerializer
from .models import *

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']        