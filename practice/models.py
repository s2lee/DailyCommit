from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='book')
    author = models.CharField(max_length=15)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
