from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer

from .models import User

class SignUpView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class   = UserSerializer