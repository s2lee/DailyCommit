from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='book')
    author = models.CharField(max_length=15)
    create_at = models.DateTimeField(auto_now_add=True)  # 최초 저장(insert) 시에만 현재날짜(date.today()) 를 적용해 기(갱신불가능)
    update_at = models.DateTimeField(auto_now=True)  # django model 이 save 될 때마다 현재날짜(date.today()) 로 갱신

    objects = models.Manager()
