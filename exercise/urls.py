from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path('book', views.book_list, name='book-list'),
    path('book/<int:pk>', views.book_detail, name='book-detail'),
    path('book/post', views.book_post, name='book-post'),
    path('book/update/<int:pk>', views.book_update, name='book-update'),
    path('book/delete/<int:pk>', views.book_delete, name='book-delete'),
    path('cbv_book', views.BookListView.as_view(), name='cbv-book-list'),
    path('cbv_book/<int:pk>', views.BookDetailView.as_view(), name='cbv-book-detail'),
    path('cbv_book/post', views.BookCreateView.as_view(), name='cbv-book-post'),
    path('cbv_book/update/<int:pk>', views.BookUpdateView.as_view(), name='cbv-book-update'),
    path('cbv_book/delete/<int:pk>/', views.BookDeleteView.as_view(), name='cbv-book-delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
