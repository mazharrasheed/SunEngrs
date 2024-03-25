"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path

from SunEngrs import settings
from home.views.contactus import contact, manufacturing
from home.views.home import Index
from home.views.products import Product

urlpatterns = [
    path('',            Index.as_view(),                        name='homepage'),
    path('products/',   Product.as_view(),                      name='homepage'),
    path('contactus/',  contact,                              name='contactus'),
    path('manufacturing/',  manufacturing,                              name='manufacturing'),
    # path('product_detail/<int:id>', product_detail,              name='product_detail'),

     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
