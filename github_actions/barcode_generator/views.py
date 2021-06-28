"""
Module to define the api to interact with barcode_generator generator model
"""
from rest_framework.viewsets import ModelViewSet

from .models import BarCodeGenerator
from .serializers import BarCodeGeneratorSerializer


class BarCodeGeneratorAPI(ModelViewSet):
    """
    Api to handle creation of barcode_generator
    """
    serializer_class = BarCodeGeneratorSerializer
    queryset = BarCodeGenerator.objects.all()
