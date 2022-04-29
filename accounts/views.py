from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer

class SignUpView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    
    def post(self, request):
        return self.create(request)