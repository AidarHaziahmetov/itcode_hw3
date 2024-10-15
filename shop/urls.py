from django.contrib import admin
from django.urls import path
from shop.views import display_image, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
urlpatterns = [
    path("catalog/", ProductListView.as_view(), name="catalog"),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]