"""
URL configuration for clothing_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from clothing_shop.settings import MEDIA_URL
from shop import views
from django.urls import path, include
from shop import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()

router.register('categories', views.CategoryAPI, basename='categories')
router.register('products', views.ProductAPI, basename='products')
urlpatterns = [
    path(MEDIA_URL, views.display_image, name='display_image'),
    path("admin/", admin.site.urls),
    path("schema/",SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("catalog/", views.ProductListView.as_view(), name="catalog"),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', views.ProductDeleteView.as_view(), name='product_delete'),

] + router.urls
