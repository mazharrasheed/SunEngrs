from django import forms

from .models.contactus import Contactus


class Contact_Form(forms.ModelForm):

    class Meta:
        model=Contactus

        fields=["name","email","phone","desc"]