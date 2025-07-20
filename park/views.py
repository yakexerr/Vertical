from django.shortcuts import render
from rest_framework import viewsets
from .models import Park
from .serializers import ParkSerializer

class ParkViewSet(viewsets.ModelViewSet):
    queryset = Park.objects.all().order_by('-id')
    serializer_class = ParkSerializer