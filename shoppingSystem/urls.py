"""shoppingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.users import views
from shoppingSystem import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_reg/', views.user_register, name='register'),
    path('user_login/', views.user_login, name='login'),
    path('ajax_login_data/', views.ajax_login_data),
    path('user_logout/', views.user_logout, name='logout'),
    path('ajax_logout_data/', views.ajax_logout_data),
    path('user_change_password/', views.change_password, name='change_password'),
    path('', include('apps.basic.urls')),
    path('products/', include('apps.goods.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
