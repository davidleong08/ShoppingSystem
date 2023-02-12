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
        fields = ['name', 'category', 'price', 'publication_date', 'publisher', 'language', 'ISBN_13', 'property5',
                  'property6', 'customer_rating', 'review', 'main_image',
                  'temporary_status', 'photo1',
                  'photo2', 'photo3', 'photo4',
                  ]
        labels = {
            "name": "name",
            "category": "product_category",
            "price": "product_price",
            "publication_date": "publication_date",
            "publisher": "publisher",
            "language": "language",
            "ISBN_13": "ISBN_13",
            "property5": "property5",
            "property6": "property6",
            "customer_rating": "customer_rating",
            "review": "review",
            "main_image": "product_main_image",
            "temporary_status": "temporary_status",
            "photo1": "photo1",
            "photo2": "photo2",
            "photo3": "photo3",
            "photo4": "photo4",
        }
        widgets = {
            "name": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "price": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "publication_date": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "publisher": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "language": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "ISBN_13": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "property5": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "property6": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "main_image": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "category": forms.widgets.Select(attrs={
                "class": "form-control"
            }),
            "customer_rating": forms.widgets.Select(attrs={
                "class": "form-control"
            }),
            "temporary_status": forms.widgets.Select(attrs={
                "class": "form-control"
            }),
            "photo1": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "photo2": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "photo3": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "photo4": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "review": forms.widgets.Textarea(attrs={
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
            "publication_date": {'required': 'the publication_date of product cannot be empty',
                          'max_length': 'the max length of publication_date is 5000'},
            "publisher": {'required': 'the publisher of product cannot be empty',
                          'max_length': 'the max length of publisher is 5000'},
            "language": {'required': 'the language of product cannot be empty',
                          'max_length': 'the max length of language is 5000'},
            "ISBN_13": {'required': 'the ISBN_13 of product cannot be empty',
                          'max_length': 'the max length of ISBN_13 is 5000'},
            "property5": {'required': 'the property5 of product cannot be empty',
                          'max_length': 'the max length of property5 is 5000'},
            "property6": {'required': 'the property6 of product cannot be empty',
                          'max_length': 'the max length of property6 is 5000'},
            "createDate": {'required': 'the create date of product cannot be empty'},
        },

    def clean(self):
        new_product_name = self.cleaned_data.get('name')
        products = Product.objects.all()
        for product in products:
            if product.name == new_product_name:
                self.add_error("name", ValidationError("the product name has been existed"))


class ProductInfoChange(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'publication_date', 'publisher', 'language', 'ISBN_13', 'property5',
                  'property6', 'customer_rating', 'review', 'main_image',
                  'temporary_status', 'photo1',
                  'photo2', 'photo3', 'photo4',
                  ]
        labels = {
            "name": "name",
            "category": "product_category",
            "price": "product_price",
            "publication_date": "publication_date",
            "publisher": "publisher",
            "language": "language",
            "ISBN_13": "ISBN_13",
            "property5": "property5",
            "property6": "property6",
            "customer_rating": "customer_rating",
            "review": "review",
            "main_image": "product_main_image",
            "temporary_status": "temporary_status",
            "photo1": "photo1",
            "photo2": "photo2",
            "photo3": "photo3",
            "photo4": "photo4",
        }
        widgets = {
            "name": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "price": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "publication_date": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "publisher": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "language": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "ISBN_13": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "property5": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "property6": forms.widgets.TextInput(attrs={
                "class": "form-control"
            }),
            "main_image": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "category": forms.widgets.Select(attrs={
                "class": "form-control"
            }),
            "customer_rating": forms.widgets.Select(attrs={
                "class": "form-control"
            }),
            "temporary_status": forms.widgets.Select(attrs={
                "class": "form-control"
            }),
            "photo1": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "photo2": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "photo3": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "photo4": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "review": forms.widgets.Textarea(attrs={
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
            "publication_date": {'required': 'the publication_date of product cannot be empty',
                          'max_length': 'the max length of publication_date is 5000'},
            "publisher": {'required': 'the publisher of product cannot be empty',
                          'max_length': 'the max length of publisher is 5000'},
            "language": {'required': 'the language of product cannot be empty',
                          'max_length': 'the max length of language is 5000'},
            "ISBN_13": {'required': 'the ISBN_13 of product cannot be empty',
                          'max_length': 'the max length of ISBN_13 is 5000'},
            "property5": {'required': 'the property5 of product cannot be empty',
                          'max_length': 'the max length of property5 is 5000'},
            "property6": {'required': 'the property6 of product cannot be empty',
                          'max_length': 'the max length of property6 is 5000'},
            "createDate": {'required': 'the create date of product cannot be empty'},
        },


class ProductPhotoChange(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['main_image', 'photo1', 'photo2', 'photo3', 'photo4']
        labels = {
            "main_image": "main_image",
            "photo1": "photo1",
            "photo2": "photo2",
            "photo3": "photo3",
            "photo4": "photo4",
        }
        widgets = {
            "main_image": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "photo1": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "photo2": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "photo3": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
            "photo4": forms.widgets.FileInput(attrs={
                "class": 'custom-file-input'
            }),
        }
