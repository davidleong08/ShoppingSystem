from django.conf.urls.static import static
from django.urls import path, include
from apps.goods import views
from shoppingSystem import settings

urlpatterns = [
    path('', views.product_view, name='products'),
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('ajax_products/', views.ajax_products)
]

