from django.contrib.auth import authenticate, login, logout

from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthFormSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = AuthFormSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.create_user(**serializer.validated_data)
                return Response(status=status.HTTP_201_CREATED)
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
                next_url = '/'
                if 'next' in request.GET:
                    next_url = request.GET.get("next")
                return Response({"next_url": next_url}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)