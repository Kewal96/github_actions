"""
Unit tests for barcode generator api query operation
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import BarCodeGenerator


class BarcodeGeneratorAPIQueryTest(APITestCase):
    """
    Test cases to demonstrate query operation for barcode generator API
    """

    def setUp(self):
        """
        Setup to create Test data
        """
        super().setUp()
        self.barcode = BarCodeGenerator.objects.create(data='123456789012')

    def test_query_barcode_generator_api_when_executed_with_valid_identifier_returns_a_record_with_expected_data_successfully(self):
        """
        Given that we have some existing barcode generator records in the database
        When query API is executed with a valid identifier
        Then API shall return 200(HTTP OK) as response status code
        And API shall return barcode information for the queried identifier
        """
        url = reverse('generate-barcodes-detail', kwargs={"pk": self.barcode.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'], self.barcode.data)
        barcode_data = BarCodeGenerator.objects.get(data=response.data['data'])
        self.assertEqual(self.barcode.image, barcode_data.image)

    def test_query_barcode_generator_api_when_executed_returns_multiple_records_with_expected_data_successfully(self):
        """
        Given that we have a one pseudo barcode generator record in database
        And a new pseudo record is created before making a request
        When query API is executed
        Then API shall return 200(HTTP OK) as response status code
        And API shall return 2 barcode records
        """
        barcode_data = BarCodeGenerator.objects.create(data='098765432123')
        url = reverse('generate-barcodes-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_query_barcode_generator_api_when_executed_with_invalid_identifier_returns_not_found_response(self):
        """
        Given that we have some existing pseudo barcode generator records in database
        When query API is executed with invalid identifier
        Then API shall return 404(HTTP NOT_FOUND) as response status code
        """
        url = reverse('generate-barcodes-detail',
                      kwargs={"pk": "invalid pk"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
