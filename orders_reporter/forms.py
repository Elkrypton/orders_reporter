from django import forms
import pyqrcode
from django import forms
from .models import Manufacturer, Note
class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = ['parts', 'order_number', 'order_date', 'sku', 'sku', 'location']
        widgets = {
            'parts': forms.TextInput(attrs={'size':'40', 'class': 'form-control'}),
            'order_number': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
            'order_date': forms.widgets.DateInput(attrs={'type': 'date'}),

            'sku': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
            'location': forms.TextInput(attrs={'size':'40','class': 'form-control'})}


class NoteForm(forms.ModelForm):

    class Meta:

        model = Note
        fields = ['name','feedback']
        widgets = {
        'name':forms.TextInput(attrs={'size':'40', 'class': 'form-control'}),
        'feedback': forms.Textarea()}


