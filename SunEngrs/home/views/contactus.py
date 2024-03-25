from datetime import datetime

from django.contrib import messages
from django.shortcuts import render

from home.forms import Contact_Form

from ..models.contactus import Contactus


def contact(request):
    data={}

    if  request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        form=Contact_Form(request.POST)
        mycontact=Contactus(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        mycontact.save()
        messages.success(request,"Success! Your massage has been sent")
        form=Contact_Form()
    else: 
        form=Contact_Form()
        
    data={'form':form}
    return render(request,'contact.html',data)


def manufacturing (request):

    data={}
  
    return render(request,'manufacturing.html',data)