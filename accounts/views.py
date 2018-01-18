from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

from .forms import VerifiedPhoneForm

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def VerifiedPhone(request):
    form = VerifiedPhoneForm(request.POST or None)
    if form.is_valid():
        phone_number = form.cleaned_data['phone_number']
        try:
            response = client.lookups.phone_numbers(phone_number).fetch(type="carrier")
            print("vaild")
            send_code(request,phone_number)
        except TwilioRestException as e:
            if e.code == 20404:
                raise Exception("not vaild")
            else:
                raise e
    return render(request, 'accounts/phone.html',{'form':VerifiedPhoneForm()})

def send_code(request,phone_number):
    print(phone_number)
    return HttpResponse(phone_number)

