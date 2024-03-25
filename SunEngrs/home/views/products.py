from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View

from ..models.category import Category
from ..models.products import Products


class Product(View):

   def get(self,request):

      products=None
      categories=Category.get_all_category()
      categoryID=(request.GET.get('category'))
      if categoryID:
         products=Products.get_all_produts_by_categoryid(categoryID)
      else:
            products=Products.get_all_produts()
      data={'products':products,'categories':categories}
      return render(request,"products.html",data)    

# def product_detail(request,id):

#    if request.method=='GET':
#       product=Products.objects.get(id=id)
#       data={'product':product}
#       return render(request,'pdetail.html',data)
      
#    else:
#       data={'product':'product'}
#       return render(request,'pdetail.html',data)
#       pass
