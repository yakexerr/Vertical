from rest_framework import serializers
from .models import Park, Entertainment, EntertainmentPhoto

class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = '__all__'

class EntertainmentDetialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entertainment
        fields = '__all__'
        depth = 1 
        '''для всех полей ForeignKey показываем не id, 
        а на уровень ниже идём и показываем весь связанный объект целиком'''

class EntertainmentPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntertainmentPhoto
        fields = ['id', 'photo']


class EntertainmentSerializer(serializers.ModelSerializer):
    photos = EntertainmentPhotoSerializer(source='entertainmentphoto_set', many=True, read_only=True)
    class Meta:
        model = Entertainment
        fields = ['id', 'title', 'description', 'min_height', 'price', 'park', 'photos']
