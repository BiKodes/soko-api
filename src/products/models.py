from django.db import models
from src.users.models import User

class Category(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


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


class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)


class Cart(models.Model):
    cart_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['cart_id', '-created_at']
        

    def __str__(self):
        return f'{self.cart_id}'