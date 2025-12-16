
from django.utils import timezone
from rest_framework import serializers


def validate_title(value):
    value = value.strip()
    if len(value) < 2:
        raise serializers.ValidationError("Title en az 2 karakter olmalı.")
    return value


def validate_rating(value):
    if value < 0 or value > 10:
        raise serializers.ValidationError("Rating 0 ile 10 arasında olmalı.")
    return value


def validate_duration(value):
    if value is None:
        return value
    if value <= 0:
        raise serializers.ValidationError("Duration 0'dan büyük olmalı.")
    return value


def validate_release_date(value):
    if value and value > timezone.now().date():
        raise serializers.ValidationError("Release date gelecekte olamaz.")
    return value