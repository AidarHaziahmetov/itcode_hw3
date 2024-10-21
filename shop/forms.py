from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from shop.models import Product, Category, User


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','description','price']
