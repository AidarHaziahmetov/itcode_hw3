import factory
from factory.django import ImageField

from shop import models


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    class Meta:
        model = models.Category

class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    image = ImageField()
    category = factory.RelatedFactory(CategoryFactory)
    description = factory.Faker('text')
    stock = factory.Faker('random_int')
    price = factory.Faker('random_int')
    created = factory.Faker('date_time')
    updated = factory.Faker('date_time')

    class Meta:
        model = models.Product
