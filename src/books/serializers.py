from rest_framework import serializers

from .models import Book
from src.users.models import User

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