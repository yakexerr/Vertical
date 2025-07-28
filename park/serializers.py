from rest_framework import serializers
from .models import Park, Entertainment

class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = '__all__'

class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entertainment
        fields = '__all__'