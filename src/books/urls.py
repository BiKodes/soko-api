from django.urls import path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name="books_app"

from .views import (
    ListBook, 
    DetailBook, 
)

schema_view = get_schema_view(
   openapi.Info(
      title="e-Commerce API",
      default_version='v1',
      description="E-Commerce API developed with Django and Django Rest Framework",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    
    path('books', ListBook.as_view(), name='books'),
    path('books/<int:pk>/', DetailBook.as_view(), name='singlebook'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]