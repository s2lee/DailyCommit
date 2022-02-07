from django import forms

from .models import Category, Book


class BookForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = ('title', 'category', 'author')

