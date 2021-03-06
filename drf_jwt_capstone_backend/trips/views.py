from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Trips
from .serializers import TripsSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TripsList(APIView):

    def get(self, request):
        trips = Trips.objects.all()
        serializer = TripsSerializer(trips, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TripsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TripDetail(APIView):

    def get_object(self, pk):
        try:
            return Trips.objects.get(pk=pk)
        except Trips.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        trips = self.get_object(pk)
        serializer = TripsSerializer(trips)
        return Response(serializer.data)

    def put(self, request, pk):
        update_trips = self.get_object(pk)
        serializer = TripsSerializer(update_trips, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, rquest, pk):
        delete_trips = self.get_object(pk)
        delete_trips.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)