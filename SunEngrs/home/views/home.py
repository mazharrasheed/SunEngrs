
from django.shortcuts import render
from django.views import View

from ..models.category import Category
from ..models.products import Products


class Index(View):

   def get(self,request):
      
      products=None
      categoryID=(request.GET.get('category'))
      if categoryID:
         products=Products.get_all_produts_by_categoryid(categoryID)
      else:
            products=Products.get_all_produts()
            
      data={'products':products}
      return render(request,"index.html",data)    

def product_detail(request,id):

   if request.method=='GET':
      product=Products.objects.get(id=id)
      data={'product':product}
      return render(request,'pdetail.html',data)
      
   else:
      data={'product':'product'}
      return render(request,'pdetail.html',data)
      pass
