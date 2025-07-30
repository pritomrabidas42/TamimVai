from django.urls import path
from .api_views import ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path('product/', ProductListAPIView.as_view(), name='api-product-list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='api-product-detail'),
]
