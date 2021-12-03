from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Replies
from .serializers import RepliesSerializer

# Create your views here.
class RepliesList(APIView):

    def get(self, request):
        replies = Replies.objects.all()
        serializer = RepliesSerializer(replies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RepliesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReplyDetail(APIView):

    def get_object(self, pk):
        try:
            return Replies.objects.get(pk=pk)
        except Replies.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        reply = self.get_object(pk)
        serializer = RepliesSerializer(reply)
        return Response(serializer.data)

    def put(self, request, pk):
        update_reply = self.get_object(pk)
        serializer = RepliesSerializer(update_reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, rquest, pk):
        delete_reply = self.get_object(pk)
        delete_reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)