from django.urls import reverse
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from .models import *
from .views import *


class APIBasicTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.category = Category.objects.create(name='test category')
        self.data = {
            'title': 'Zero to One',
            'category': self.category.id,
            'author': 'Peter Thiel'
        }
        self.book = Book.objects.create(title='Zero to One',
                                        category=self.category,
                                        author='Peter Thiel')

    def test_get_book_list(self):
        response = self.client.get(reverse('book-list'), format='json')
        response2 = self.client.get('/fbv_api/book', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

        request = self.factory.get('/fbv_api/book')
        response3 = book_list(request)
        self.assertEqual(response3.status_code, status.HTTP_200_OK)

    def test_post_book_list(self):
        book_count = Book.objects.all().count()
        response = self.client.post(reverse('book-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.all().count(), book_count + 1)

        new_book = Book.objects.latest('id')
        self.assertEqual(new_book.title, self.data['title'])

        request = self.factory.post(reverse('cbv-book-list'), self.data, format='json')
        response2 = BookListAPIView.as_view()(request)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)

    def test_detail_book(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Zero to One')

    def test_update_book(self):
        response = self.client.put(reverse('book-detail', kwargs={'pk': 1}),
                                   {'title': 'Nudge', 'category': self.category.id, 'author': 'RiChard'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['author'], 'RiChard')