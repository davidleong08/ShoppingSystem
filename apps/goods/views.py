import json

from django.shortcuts import render
from apps.goods.models import Product, ProductsCategory
from django.http import HttpResponse, JsonResponse
from django.core import serializers


# Create your views here.
def product_view(request):
    products = Product.objects.all()
    categorys = ProductsCategory.objects.all()
    return render(request, "product_show.html", {"products": products, "categorys": categorys})


def product_detail(request, product_id):
    product = Product.objects.filter(product_id=product_id)
    img_url = product[0].main_image
    return render(request, "product_detail.html", {"product": product, "img_url": img_url})


def ajax_products(request):
    print(request.GET)
    product_name = request.GET.get("name", '')
    category_id = request.GET.get("category_id", '')
    temporary_status = request.GET.get("temporary_status", '')
    print(product_name, temporary_status)
    page_size = 2
    page = int(request.GET["page"])
    total = Product.objects.filter(name=product_name,
                                   temporary_status=temporary_status).count()
    products = Product.objects.filter(name=product_name,
                                      temporary_status=temporary_status).order_by("product_id")[
               (page - 1) * page_size: page * page_size]
    rows = []
    for product in products:
        rows.append({
            "product_id": product.product_id,
            "name": product.name,
            "temporary_status": product.temporary_status,
            "category_id": product.category.name,
            "price": product.price,
            "property1": product.property1,
            "property2": product.property2,
            "sale_number": product.sale_number,
            "sale_amount": product.sale_amount,
            "customer_rating": product.customer_rating,
            "review": product.review,
            "createDate": product.createDate
        })

    datas = {"total": total, "rows": rows}
    print(datas)
    return JsonResponse(datas, safe=False, json_dumps_params={'ensure_ascii': False, "indent": 4})
