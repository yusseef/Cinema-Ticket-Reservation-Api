from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import status, filters
from .models import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, viewsets
# Create your views here.

                        #Movies FBV
@api_view(['GET', 'POST'])
def movielist(request):
    try:
        guest = Guest.objects.all()
    except guest.DoesNotExist:
        raise Http404
    
    if request.method == 'POST':
        serializer = GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_406_NOT_ACCEPTABLE)
    
    if request.method == 'GET':
        serializer = GuestSerializer(guest, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_pk(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = GuestSerializer(guest, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        guest.delete()
        return Response(status = status.HTTP_200_OK)

                                #Hall CBV

class ListHalls(APIView):

    def get(self, request):
        hall = Hall.objects.all()
        if hall:
            serializer = HallSerializer(hall, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = HallSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(status = status.HTTP_204_NO_CONTENT)

class HallPk(APIView):
    def get_object(self, pk):
        try:
            return Hall.objects.get(pk = pk)
        except Hall.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        hall = self.get_object(pk)
        serializer = HallSerializer(hall)
        return Response(serializer.data, status = status.HTTP_302_FOUND)

    def put(self, request, pk):
        hall = self.get_object(pk)
        serializer = HallSerializer(hall, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, pk):
        hall = self.get_object(pk)
        hall.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

                    #GuestGeneridCBV

class GuestList(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class GuestPk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer



                #Viewsets reservation

class Reservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends  = [filters.SearchFilter]
    search_fields = ['guest__name']

        

    