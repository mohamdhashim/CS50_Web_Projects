from django.forms import ModelForm,widgets
from auctions.models import Listings
from django.forms.widgets import *


class newProductForm(ModelForm):
    class Meta:
        model = Listings
        fields = ['title','start_bid', 'description','image']
        widgets = {

        'description':  Textarea(attrs = {
            'class': "form-control", 
            'style': 'max-width: 400px;'
            }),     

        'title': TextInput(attrs={
            'class': "form-control",
            'style': 'max-width: 400px;',
            'placeholder': 'Name'
            }),
        'start_bid': NumberInput(attrs = {
            'class': "form-control", 
            'style': 'max-width: 300px;'
            }),



        'image': FileInput(attrs = {
            'class': "btn btn-primary", 
            }),             
        }