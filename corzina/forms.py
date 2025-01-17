from django import forms
from . import models

class Corzina(forms.ModelForm):
    class Meta:
        model = models.ShoppingCart
        fields = '__all__'