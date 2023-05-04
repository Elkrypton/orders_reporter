from django import forms
import pyqrcode
from django import forms
from .models import Manufacturer
class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Manufacturer
<<<<<<< HEAD
        fields = ['parts', 'order_number', 'order_date', 'sku', 'sku', 'location']
        widgets = {
            'parts': forms.TextInput(attrs={'size':'40', 'class': 'form-control'}),
            'order_number': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
            'order_date': forms.widgets.DateInput(attrs={'type': 'date'}),

            'sku': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
=======
        fields = ['vendor', 'model', 'store_sku', 'omsid', 'store_so_sku', 'parts_usage','location']
        widgets = {
            'vendor': forms.TextInput(attrs={'size':'40', 'class': 'form-control'}),
            'model': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
            'store_sku': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
            'omsid': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
            'store_so_sku': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
            'parts_usage': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
>>>>>>> 5aba71bbc6b139b60dcc33661d0611782daf2da2
            'location': forms.TextInput(attrs={'size':'40','class': 'form-control'})}
