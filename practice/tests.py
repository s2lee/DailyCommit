from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class APIBasicTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.data = {
            'title': 'test_title',
            'category': 2,
            'author': 'test_author'
        }

    def test_book_list(self):
        response = self.client.post(reverse('book-list'), self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
