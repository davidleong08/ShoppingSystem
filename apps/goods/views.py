from django.shortcuts import render
from apps.goods.models import Product, ProductsCategory


# Create your views here.
def product_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def product_detail(request, product_id):
    product = Product.objects.filter(product_id=product_id)
    img_url = product[0].main_image
    return render(request, "product_detail.html", {"product": product, "img_url": img_url})

