from rest_framework.serializers import  ModelSerializer
from .models import *

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'image']