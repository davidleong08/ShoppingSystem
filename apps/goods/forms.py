from django.core.exceptions import ValidationError
from django import forms
from apps.goods.models import ProductsCategory, Product


class ProductsCategoryInfo(forms.ModelForm):
    class Meta:
        model = ProductsCategory
        fields = ['name']
        labels = {
            "name": "product_category_name"
        }
        error_messages = {
            "name": {'required': 'the product category name cannot be empty'}
        }

    def clean_name(self):
        new_name = self.cleaned_data.get('name')
        product_categories = ProductsCategory.objects.all()
        for productCategory in product_categories:
            if productCategory.name == new_name:
                self.add_error("name", ValidationError("the product category has been existed"))


class ProductInfo(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'property1', 'property2', 'sale_number', 'sale_amount',
                  'customer_rating', 'review', 'main_image', 'temporary_status', 'photo1', 'photo2', 'photo3', 'photo4',
                  'createDate']
        labels = {
            "name": "product_name",
            "category": "product_category",
            "price": "product_price",
            "property1": "property1",
            "property2": "property2",
            "sale_number": "sale_number",
            "sale_amount": "sale_amount",
            "customer_rating": "customer_rating",
            "review": "review",
            "main_image": "product_main_image",
            "temporary_status": "temporary_status",
            "photo1": "photo1",
            "photo2": "photo2",
            "photo3": "photo3",
            "photo4": "photo4",
            "createDate": "product_createDate",
        }
        widgets = {
            "main_image": forms.widgets.FileInput(attrs={
                "class": "form-control"
            }),
            "category": forms.widgets.Select(attrs={
                "class": "form-control"
            }),
        }
        error_messages = {
            "name": {'required': 'the product name cannot be empty',
                     'max_length': 'the max length of product name is 50'},
            "category": {'required': 'the product category cannot be empty'},
            "price": {'required': 'the product price cannot be empty',
                      'max_digits': 'the max digits of product price is 32',
                      'decimal_places': 'the decimal place of product price is 8'},
            "property1": {'required': 'the property1 of product cannot be empty',
                          'max_length': 'the max length of property1 is 100'},
            "property2": {'required': 'the property2 of product cannot be empty',
                          'max_length': 'the max length of property2 is 100'},
            "sale_number": {'required': 'the sale number of product cannot be empty'},
            "sale_amount": {'required': 'the sale amount of product cannot be empty'},
            "createDate": {'required': 'the create date of product cannot be empty'},
        },

    def clean_name(self):
        new_product_name = self.cleaned_data.get('name')
        products = Product.objects.all()
        for product in products:
            if product.name == new_product_name:
                self.add_error("name", ValidationError("the product name has been existed"))
