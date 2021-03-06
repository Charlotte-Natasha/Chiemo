from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.http import HttpResponse
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


# Create your views here.
class ProfileView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                        context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'user_id': user.pk,
            'email': user.email,
        })

class MenuView(generics.ListCreateAPIView):

    serializer_class = MenuSerializer

    queryset = Menu.objects.all()  

    def post(self, request, *args, **kwargs):
        name = request.data['name']   
        image = request.data['image'] 
        Menu.objects.create(name=name, image=image) 
        return HttpResponse({'message': 'Menu uploaded'}, status=200)

class CategoryView(generics.ListCreateAPIView):

    serializer_class = CategorySerializer

    queryset = Category.objects.all()        