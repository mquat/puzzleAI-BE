from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User

class UserSerializer(serializers.Serializer):
    email      = serializers.EmailField(validators = [UniqueValidator(queryset = User.objects.all())])
    last_name  = serializers.CharField(max_length = 50, write_only = True) 
    first_name = serializers.CharField(max_length = 50, write_only = True)
    password   = serializers.CharField(max_length= 128, write_only = True) 

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email    = serializers.EmailField()
    password = serializers.CharField(max_length = 128, write_only = True)

    def validate(self, data):
        email    = data.get('email', None)
        password = data.get('password', None)
        
        user = authenticate(username = email, password = password)

        if not user: 
            raise serializers.ValidationError('Invalid User')

        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated')

        return {'user' : user}