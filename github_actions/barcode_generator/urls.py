from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BarCodeGeneratorAPI

router = DefaultRouter()

router.register('generate-barcodes', BarCodeGeneratorAPI, basename='generate-barcodes')

urlpatterns = [
    path('', include(router.urls))
]
