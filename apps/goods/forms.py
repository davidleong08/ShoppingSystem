from django.core.exceptions import ValidationError
from django import forms
from apps.goods.models import ProductsCategory, Product


class ProductsCategoryInfo(forms.ModelForm):
    class Meta:
        model = ProductsCategory
        fields = ['']