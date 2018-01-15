from django import forms
from .models import ServiceAdd

class ServiceAddForm(forms.ModelForm):
    class Meta:
        model = ServiceAdd
        fields = '__all__'
