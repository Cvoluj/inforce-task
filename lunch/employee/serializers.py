from rest_framework import serializers
from .models import Employee, MyUserManager
from rest_framework_simplejwt.serializers import TokenObtainSerializer

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = Employee
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        return Employee.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)
    
    class Meta:
        model = Employee
        fields = ['email', 'username', 'password', 'token']

        read_only_fields = ['token']
    
