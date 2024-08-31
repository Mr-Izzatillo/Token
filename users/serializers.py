from .models import User
from rest_framework import serializers



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']



class LoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField()
    password = serializers.CharField()
        
        

class ResetPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = ['id', 'username', 'first_name', 'last_name', 'phone_number']
        