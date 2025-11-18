
from django import forms
from .models import Product
from .models import ShippingAddress

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['full_name', 'address', 'city', 'phone']
