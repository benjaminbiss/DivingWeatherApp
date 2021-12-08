from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users
from .serializers import UsersSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UsersList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        users = self.get_object(pk)
        serializer = UsersSerializer(users)
        return Response(serializer.data)

    def put(self, request, pk):
        update_users = self.get_object(pk)
        serializer = UsersSerializer(update_users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, rquest, pk):
        delete_users = self.get_object(pk)
        delete_users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)