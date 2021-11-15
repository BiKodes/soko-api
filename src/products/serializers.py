from rest_framework import serializers
from .models import Category, Book, Product, Cart
from src.users.models import User


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category 


class BookSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username', read_only=False)

    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'author',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'imageUrl',
            'created_by',
            'status',
            'date_created'
        )
        model = Book

class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username', read_only=False)
    class Meta:
        fields = (
            'id',
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            'imageUrl',
            'created_by',
            'status',
            'date_created'
        )
        model = Product


class CartUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class CartSerializer(serializers.ModelSerializer):

    cart_id = CartUserSerializer(read_only=True, many=False)
    books = BookSerializer(read_only=True, many=True)
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = ('cart_id', 'created_at', 'books', 'products')