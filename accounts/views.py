from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import UserSerializer, LoginSerializer

class SignUpView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class   = UserSerializer

class LogInView(ObtainAuthToken):
    permission_classes = [AllowAny]
    serializer_class   = LoginSerializer