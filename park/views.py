from django.shortcuts import render
from rest_framework import viewsets
from .models import Park, Entertainment
from .serializers import ParkSerializer, EntertainmentSerializer

class ParkViewSet(viewsets.ModelViewSet):
    queryset = Park.objects.all().order_by('-id')
    serializer_class = ParkSerializer

class EntertainmentViewSet(viewsets.ModelViewSet):
    queryset = Entertainment.objects.order_by('-id')
    serializer_class = EntertainmentSerializer