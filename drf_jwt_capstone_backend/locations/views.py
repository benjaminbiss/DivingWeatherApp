from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Locations
from .serializers import LocationSerializer

# Create your views here.
class LocationList(APIView):

    def get(self, request):
        locations = Locations.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetail(APIView):

    def get_object(self, pk):
        try:
            return Locations.objects.get(pk=pk)
        except Locations.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, pk):
        update_location = self.get_object(pk)
        serializer = LocationSerializer(update_location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, rquest, pk):
        delete_location = self.get_object(pk)
        delete_location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)