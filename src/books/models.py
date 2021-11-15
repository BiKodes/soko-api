from django.db import models
from src.users.models import User
from src.products.models import Category


class Book(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    author = models.CharField(max_length=150, default='Nuru Hekima')
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title