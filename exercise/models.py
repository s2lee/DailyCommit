from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='book')
    author = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    objects = models.Manager()