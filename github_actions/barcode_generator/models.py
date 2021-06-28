"""
Module to represent the Barcode Generator module model
"""
from io import BytesIO

import barcode
from barcode.writer import ImageWriter
from django.core.files import File
from django.db import models


class BarCodeGenerator(models.Model):
    """
    Data model to represent the Barcode Generator to generate barcode_generator based on given data.
    """
    data = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')

    def save(self, *args, **kwargs):  # overriding save()
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.data}', writer=ImageWriter()).write(rv)
        self.image.save(f'{self.data}.png', File(rv), save=False)
        return super().save(*args, **kwargs)
