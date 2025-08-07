from django.shortcuts import render
from rest_framework import viewsets
from .models import Park, Entertainment
from .serializers import ParkSerializer, EntertainmentSerializer
from .tasks import notify_admin_of_new_entertainment

class ParkViewSet(viewsets.ModelViewSet):
    queryset = Park.objects.all().order_by('-id')
    serializer_class = ParkSerializer

class EntertainmentViewSet(viewsets.ModelViewSet):
    queryset = Entertainment.objects.order_by('-id')
    serializer_class = EntertainmentSerializer

    # "влезли" в процесс создания объекта
    def perform_create(self, serializer):
        entertainment_instance = serializer.save() # сохраняет объект и возвращает нам эксемпляр
        notify_admin_of_new_entertainment.delay(entertainment_instance.id) # Мы немедленно вызываем нашу задачу, передав ей ID только что созданного развлечения