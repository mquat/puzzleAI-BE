from MySQLdb import DataError
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