from django.contrib.auth import authenticate, login, logout

from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthFormSerializer, UserSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = AuthFormSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.create_user(**serializer.validated_data)
                user_serializer = UserSerializer(user)
                return Response(status=status.HTTP_201_CREATED, data=user_serializer.data)
            except Exception as e:
                message = 'Please correct the errors'
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = AuthFormSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, **serializer.validated_data)
            if user is None:
                message = "Invalid email or password"
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
            else:
                login(request, user)
                user_serializer = UserSerializer(user)
                return Response(status=status.HTTP_201_CREATED, data=user_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)