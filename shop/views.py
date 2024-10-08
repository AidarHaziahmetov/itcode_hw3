from django.shortcuts import render  # noqa: F401
from PIL import Image
from django.http import HttpResponse
from django.conf import settings
import os


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
