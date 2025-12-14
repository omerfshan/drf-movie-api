from django.utils import timezone

from rest_framework import serializers
from .models import Movies

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
        read_only_fields = ['created_at']

    def validate_title(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError("Title en az 2 karakter olmalı.")
        return value

    def validate_rating(self, value):
        # DecimalField ise value Decimal gelir
        if value < 0 or value > 10:
            raise serializers.ValidationError("Rating 0 ile 10 arasında olmalı.")
        return value

    def validate_duration(self, value):
        if value is None:
            return value
        if value <= 0:
            raise serializers.ValidationError("Duration 0'dan büyük olmalı.")
        return value

    def validate_release_date(self, value):
        if value and value > timezone.now().date():
            raise serializers.ValidationError("Release date gelecekte olamaz.")
        return value

   