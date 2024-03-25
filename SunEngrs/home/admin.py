from django.contrib import admin

from .models.category import Category
from .models.contactus import Contactus
from .models.products import Products

# Register your models here.

class AdminProduct(admin.ModelAdmin):

    list_display=['product_name','pro_des','pro_price','category','pro_img']

admin.site.register(Products,AdminProduct)

class AdminCategory(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Category,AdminCategory)
admin.site.register(Contactus)

