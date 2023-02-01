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
        fields = ['name', 'market_price', 'category', 'price', 'unit', 'amount', 'goods_desc', 'main_image',
                  'stock_num', 'createDate']
        labels = {
            "name": "product_name",
            "market_price": "product_market_price",
            "category": "product_category",
            "price": "product_price",
            "unit": "product_unit",
            "amount": "product_amount",
            "goods_desc": "product_description",
            "main_image": "product_main_image",
            "stock_num": "product_stock_number",
            "createDate": "product_createDate",
        }
        widgets = {"main_image": forms.widgets.FileInput(attrs={
            "class": "form-product-image"
        }),
            "category": forms.widgets.Select(attrs={
                "class": "form-product-category"
            })}
        error_messages = {
            "name": {'required': 'the product name cannot be empty',
                     'max_length': 'the max length of product name is 50'},
            "market_price": {'required': 'the product market price cannot be empty',
                             'max_digits': 'the max digits of market price is 32',
                             'decimal_places': 'the decimal place of market price is 8'},
            "category": {'required': 'the product category cannot be empty'},
            "price": {'required': 'the product price cannot be empty',
                      'max_digits': 'the max digits of product price is 32',
                      'decimal_places': 'the decimal place of product price is 8'},
            "unit": {'required': 'the product unit cannot be empty',
                     'max_length': 'the max length of product unit is 10',
                     },
            "amount": {'required': 'the product amount cannot be empty'},
            "goods_desc": {'required': 'the product description cannot be empty',
                           'max_length': 'the max length of goods description is 5000',
                           },
            "stock_num": {'required': 'the stock number of product cannot be empty'},
            "createDate": {'required': 'the create date of product cannot be empty'}
        }

    def clean_name(self):
        new_product_name = self.cleaned_data.get('name')
        products = Product.objects.all()
        for product in products:
            if product.name == new_product_name:
                self.add_error("name", ValidationError("the product name has been existed"))

