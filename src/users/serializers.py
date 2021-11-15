from rest_framework import serializers
from rest_framework import generics

from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        read_only_fields = ('username', )


class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)


    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    def validated(self, args):
        email = args.get('email', None)
        username = args.get('username', None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('Email already exists')})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('Username already registered')})

        return super().validate(args)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'auth_token')
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}



    
