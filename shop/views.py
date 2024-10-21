import os
from typing import Type

from PIL import Image
from django.conf import settings
from django.http import HttpResponse
from django.template.backends.utils import csrf_input
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django_filters.views import FilterView

from shop.forms import ProductForm
from shop.models import Product
from shop.filters import ProductFilter


# Create your views here.


class ProductListTemplateView(TemplateView):
    template_name = "shop/product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context


class ProductListView(FilterView):
    model = Product
    template_name = "shop/product_list.html"
    context_object_name = "products"
    filterset_class: Type[ProductFilter] = ProductFilter


class ProductDetailView(DetailView):
    template_name = "shop/product_detail.html"
    model = Product
    context_object_name = "product"


class ProductCreateView(CreateView):
    template_name = "shop/product_form.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog")


class ProductUpdateView(UpdateView):
    template_name = "shop/product_form.html"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        success_url = reverse_lazy("product_detail", kwargs={"pk": self.object.pk})
        return success_url


class ProductDeleteView(DeleteView):
    template_name = "shop/product_delete.html"
    model = Product
    success_url = reverse_lazy("catalog")


