from django.contrib.auth import get_user_model
from .serializers import RegistrationSerializer
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserList(APIView):
    
        def get(self, request):
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data)