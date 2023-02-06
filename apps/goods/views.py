from django.shortcuts import render, redirect
from apps.goods.models import Product, ProductsCategory
from django.http import JsonResponse
from apps.goods.forms import ProductInfo


# Create your views here.
def user_product_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def vendor_product_view(request):
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
            "property3": product.property3,
            "property4": product.property4,
            "property5": product.property5,
            "property6": product.property6,
            "sale_number": product.sale_number,
            "sale_amount": product.sale_amount,
            "customer_rating": product.customer_rating,
            "review": product.review,
            "createDate": product.createDate
        })

    datas = {"total": total, "rows": rows}
    print(datas)
    return JsonResponse(datas, safe=False, json_dumps_params={'ensure_ascii': False, "indent": 4})


def product_add(request):
    if request.method == "GET":
        form_obj = ProductInfo()
        return render(request, 'product_add.html', {'form_obj': form_obj})
    if request.method == "POST":
        form_obj = ProductInfo(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form_obj.is_valid():
            name = request.POST.get("name", '')
            category = request.POST.get("category", '')
            price = request.POST.get("price", '')
            property1 = request.POST.get("property1", '')
            property2 = request.POST.get("property2", '')
            property3 = request.POST.get("property3", '')
            property4 = request.POST.get("property4", '')
            property5 = request.POST.get("property5", '')
            property6 = request.POST.get("property6", '')
            customer_rating = request.POST.get("customer_rating", '')
            review = request.POST.get("review", '')
            main_image = request.FILES.get("main_image", '')
            temporary_status = request.POST.get("temporary_status", '')
            photo1 = request.FILES.get("photo1", '')
            photo2 = request.FILES.get("photo2", '')
            photo3 = request.FILES.get("photo3", '')
            photo4 = request.FILES.get("photo4", '')
            products = Product.objects.filter(name=name, price=price)
            if products:
                info = "the product has been existed"
                return render(request, 'product_add.html', {"info": info})
            else:
                form_obj.cleaned_data["name"] = name
                form_obj.cleaned_data["category"] = ProductsCategory.objects.filter(category_id=category)[0]
                form_obj.cleaned_data["price"] = price
                form_obj.cleaned_data["property1"] = property1
                form_obj.cleaned_data["property2"] = property2
                form_obj.cleaned_data["property3"] = property3
                form_obj.cleaned_data["property4"] = property4
                form_obj.cleaned_data["property5"] = property5
                form_obj.cleaned_data["property6"] = property6
                form_obj.cleaned_data["sale_number"] = 0
                form_obj.cleaned_data["sale_amount"] = 0
                form_obj.cleaned_data["customer_rating"] = customer_rating
                form_obj.cleaned_data["review"] = review
                form_obj.cleaned_data["main_image"] = main_image
                form_obj.cleaned_data["temporary_status"] = temporary_status
                form_obj.cleaned_data["photo1"] = photo1
                form_obj.cleaned_data["photo2"] = photo2
                form_obj.cleaned_data["photo3"] = photo3
                form_obj.cleaned_data["photo4"] = photo4
                print(form_obj.cleaned_data)
                product = Product.objects.create(**form_obj.cleaned_data)
                info = "create product successful"
                return redirect('products')
        else:
            errors = form_obj.errors
            print(errors)
            return render(request, "product_add.html", {"form_obj": form_obj, "errors": errors})
