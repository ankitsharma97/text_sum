from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
import requests

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginUser(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        
        if not username or not password:
            return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutUser(generics.GenericAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class FindUsers(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        search_term = self.request.GET.get('search', '')
        if not search_term:
            return User.objects.none()
        
        return User.objects.filter(
            username__icontains=search_term) | User.objects.filter(
            first_name__icontains=search_term) | User.objects.filter(
            last_name__icontains=search_term) | User.objects.filter(
            email__icontains=search_term)

class SummarizeText(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        text = request.data.get('text', '')
        if not text:
            return Response({"error": "No text provided"}, status=status.HTTP_400_BAD_REQUEST)
    
        API_URL = 'https://api.meaningcloud.com/summarization-1.0'
        headers = {'Authorization': 'Bearer 196da8a772244b9cf724d75279c9681d'}
        
        payload = {
            'key': '196da8a772244b9cf724d75279c9681d',
            'txt': text,
            'sentences': 5,
        }
        
        response = requests.post(API_URL, data=payload)
    
        if response.status_code == 200:
            return Response(response.json())
        return Response(response.json(), status=response.status_code)
