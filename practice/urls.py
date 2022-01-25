from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('book', views.BookViewSet)


urlpatterns = [
    path('fbv_api/book', views.book_list, name='book-list'),
    path('fbv_api/book/<int:pk>', views.book_detail, name='book-detail'),
    path('cbv_api/book', views.BookListAPIView.as_view(), name='cbv-book-list'),
    path('cbv_api/book/<int:pk>', views.BookDetailAPIView.as_view()),
    path('mixins/book/', views.BookListMixins.as_view()),
    path('mixins/book/<int:pk>/', views.BookDetailMixins.as_view()),
    path('generic/book/<str:category>', views.BookListGenericAPIView.as_view()),
    path('generic/book-detail/<int:pk>', views.BookDetailGenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
]

