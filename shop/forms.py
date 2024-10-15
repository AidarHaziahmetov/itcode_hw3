from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from shop.models import Product, Category

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    category = ModelMultipleChoiceField(queryset=Category.objects.filter(parent__clothes__category__isnull=True),widget=CheckboxSelectMultiple())
