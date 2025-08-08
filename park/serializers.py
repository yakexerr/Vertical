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


class EntertainmentDetialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entertainment
        fields = '__all__'
        depth = 1 
        '''для всех полей ForeignKey показываем не id, 
        а на уровень ниже идём и показываем весь связанный объект целиком'''