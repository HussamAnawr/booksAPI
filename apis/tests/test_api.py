from rest_framework.test import (
    APITestCase,
    )
from rest_framework import status
from django.urls import reverse
from books.models import Book

BOOK_LIST = reverse('apis:book_list')

class APITests(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='Django for APIs',
            subtitle='Build web APIs with Python and Djando',
            author='William S. Vincent',
            isbn='9781735467221',
        )
    def test_api_listview(self):
        res = self.client.get(BOOK_LIST)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(res, self.book)