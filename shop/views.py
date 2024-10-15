import os

from PIL import Image
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from shop.forms import ProductForm
from shop.models import Product


# Create your views here.
def display_image(request, image_name):
    """Отображает скачанное изображение."""

    try:
        full_image_path = os.path.join(settings.MEDIA_ROOT, image_name)
        image_data = Image.open(full_image_path)
        response = HttpResponse(content_type="image/jpeg")
        image_data.save(response, format="JPEG")
        return response

    except FileNotFoundError:
        return HttpResponse("Изображение не найдено", status=404)


class ProductListTemplateView(TemplateView):
    template_name = "shop/product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context


class ProductListView(ListView):
    model = Product
    template_name = "shop/product_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    template_name = "shop/product_detail.html"
    model = Product
    context_object_name = "product"


class ProductCreateView(CreateView):
    template_name = "shop/product_form.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("shop:catalog")


class ProductUpdateView(UpdateView):
    template_name = "shop/product_form.html"
    model = Product
    form_class = ProductForm
    def get_success_url(self):
        success_url = reverse_lazy("shop:product_detail", kwargs={"pk": self.object.pk})
        return success_url


class ProductDeleteView(DeleteView):
    template_name = "shop/product_delete.html"
    model = Product
    success_url = reverse_lazy("shop:catalog")


def baseview(request):
    return render(request, "base.html")
