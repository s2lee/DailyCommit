from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Book
        fields = ('id', 'title', 'category_name', 'category', 'author', 'create_at', 'update_at')
