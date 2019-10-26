from rest_framework import serializers
from .models import Dolar

"""Serializer para transformación a Json de data"""
class DolarSerializer(serializers.ModelSerializer):
    class Meta:
        """Modelo Dolar con ___all___ fields"""
        model = Dolar
        fields = ('fecha', 'valor')
