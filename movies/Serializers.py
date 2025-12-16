from django.utils import timezone

from rest_framework import serializers
from .models import Movies
from . import validation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields=['id','title','category','rating','release_date']
class MovieDetails(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields='__all__'
class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = [
            'title',
            'description',
            'release_date',
            'duration',
            'rating',
            'poster',
            'category',
            'created_at',
        ]
       
    def validate_title(self, value):
        return validation.validate_title(value)

    def validate_rating(self, value):
        return validation.validate_rating(value)

    def validate_duration(self, value):
        return validation.validate_duration(value)

    def validate_release_date(self, value):
        return validation.validate_release_date(value)
    
class MovieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = [
            'title',
            'description',
            'release_date',
            'duration',
            'rating',
            'poster',
            'category',
            'created_at',
        ]
       
    def validate_title(self, value):
        return validation.validate_title(value)

    def validate_rating(self, value):
        return validation.validate_rating(value)

    def validate_duration(self, value):
        return validation.validate_duration(value)

    def validate_release_date(self, value):
        return validation.validate_release_date(value)
  

   