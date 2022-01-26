from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from .models import *
from .views import *


class APIBasicTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.category = Category.objects.create(name='test category')
        self.book = Book.objects.create(title='Zero to One',
                                        category=self.category,
                                        author='Peter Thiel')
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.id})
        self.book_count = Book.objects.all().count()

    def test_get_book_list(self):
        response = self.client.get(self.list_url, format='json')
        response2 = self.client.get('/fbv_api/book', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

        request = self.factory.get(self.list_url)
        response3 = book_list(request)
        self.assertEqual(response3.status_code, status.HTTP_200_OK)

    def test_post_book_list(self):
        data = {
            'title': 'Scale',
            'category': self.category.id,
            'author': 'Geoffrey West'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.all().count(), self.book_count + 1)

        new_book = Book.objects.latest('id')
        self.assertEqual(new_book.title, data['title'])

        request = self.factory.post(reverse('cbv-book-list'), data, format='json')
        response2 = BookListAPIView.as_view()(request)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)

    def test_detail_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Zero to One')

    def test_update_book(self):
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.id}),
                                   {'title': 'Nudge', 'category': self.category.id, 'author': 'RiChard'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['author'], 'RiChard')

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.all().count(), self.book_count - 1)
