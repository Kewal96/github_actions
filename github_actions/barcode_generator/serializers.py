"""
Serializer for handling barcode_generator generator model
"""
from rest_framework import serializers

from .models import BarCodeGenerator


class BarCodeGeneratorSerializer(serializers.ModelSerializer):
    """
    Serializer to handle data storage and retrieval of Barcode Generator model
    """
    class Meta:
        """
        Meta class to customize the serializer
        """
        model = BarCodeGenerator
        fields = ['data']
