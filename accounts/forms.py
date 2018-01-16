from django import forms


class VerifiedPhoneForm(forms.Form):
    phone_number =  forms.CharField(widget=forms.TextInput(attrs={'class': 'phone_number'}))