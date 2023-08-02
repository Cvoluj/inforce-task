from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.request import Request
from .serializers import RegisterSerializer, LoginSerializer
from employee.models import Employee
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, get_user_model
from django.conf import settings
import jwt


User = get_user_model

# Register API
class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny] # givepermission to register any, what is logical
    queryset = Employee.objects.all() 

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginAPIView(generics.GenericAPIView):

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    queryset = Employee.objects.all() 

    def post(self, request: Request) -> Response:
        username = request.data.get('userame', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        
        employee = Employee.objects.get(email=email)


        if employee.check_password(password):
            serializer = self.serializer_class(employee)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response({'message': "Invalid credentials, try again"}, status=status.HTTP_400_BAD_REQUEST)
            
class AuthUserAPIView(generics.GenericAPIView):
    permission_classes= (permissions.IsAuthenticated, )
    def get(self, request: Request) -> RegisterSerializer:
        user = request.user
        serializer = RegisterSerializer(user)

        return Response({'user': serializer.data})
       


# Create your views here.
