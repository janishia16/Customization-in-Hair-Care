from django import forms

from . models import detail

class ProductForm(forms.ModelForm):
    class Meta:
        model=detail
        fields=['image','pname','price','manufdate','expirydate']
        widgets={
            'image':forms.ImageField(attr={'class': 'form-control'}),
            'pname':forms.TextInput(attr={'class': 'form-control'}),
            'price':forms.DecimalField(attr={'class': 'form-control'}),
            'manufdate':forms.TextInput(attr={'class': 'form-control'}),
            'expirydate':forms.DateInput(attr={'class': 'form-control'}),
        }