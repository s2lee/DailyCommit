from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Book
        fields = ('id', 'title', 'category_name', 'category', 'author', 'create_at', 'update_at')

    # Object-level validation
    def validate(self, data):
        if data['title'] == data['author']:
            raise ValidationError("Title and Author must be different")
        return data

    # Field-level validation - 필드값을 value 파라미터로 받아 validation 작업을 해줌
    def validate_author(self, value):
        if not value[0].isupper():
            raise ValidationError("The first letter of the author must be uppercase")
        return value


class BookTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'author')


