from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path('book', views.book_list, name='book-list'),
    path('book/<int:pk>', views.book_detail, name='book-detail'),
    path('book/post', views.book_post, name='book-post'),
    path('book/<int:pk>/edit/', views.book_edit, name='book-edit'),
    path('cbv_book', views.BookListView.as_view(), name='cbv-book-list'),
    path('cbv_book/<int:pk>', views.BookDetailView.as_view(), name='cbv-book-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
