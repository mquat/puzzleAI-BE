from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer, LoginSerializer

from .models import User

class TokenValidateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        header = request.headers.get('Authorization')

        for token in Token.objects.all():
            if header == token.key:
                return Response({'message':'Valid token'}, status = status.HTTP_200_OK)

        return Response({'message':'Signup or Login is needed'}, status = status.HTTP_401_UNAUTHORIZED)
                
class EmailSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = User.objects.all()
        username = request.query_params.get('email')
        filter   = queryset.filter(email__icontains = username)
        if filter:
            return Response({'message':'This email already exists'}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message':'It is available'}, status = status.HTTP_202_ACCEPTED)

class SignUpView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class   = UserSerializer

class LogInView(ObtainAuthToken):
    permission_classes = [AllowAny]
    serializer_class   = LoginSerializer