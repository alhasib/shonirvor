from django.shortcuts import render, redirect
from .forms import ServiceAddForm
from .models import ServiceAdd, ServiceCatagory

def service_catagory(request):
    form=ServiceCatagory.objects.all()
    context={'form':form}
    return render(request, 'service/service_catagory.html', context)

def service_add(request):
    if request.method == 'POST':
        form = ServiceAddForm(request.POST, request.FILES)
        if form.is_valid():
            value = form.cleaned_data['provider']
            form.save()
            context = {'form':form}
            return redirect('service_details', provider=value)
    else:
        form = ServiceAddForm()
        context = {'form':form}
        return render(request,'service/service_add.html', context)

def service_details(request, provider):
    form = ServiceAdd.objects.get(provider=provider)
    context = {'form':form}
    return render(request,'service/service_details.html',context)

def catagorywise_service(request, service_catagory):
    try:
        form=ServiceAdd.objects.filter(catagory__catagory_name=service_catagory)
        context={'form':form}
    except:
        context={'errmsg':'You have no service'}
    return render(request,'service/catagorywise_service.html',context)

# Create your views here.
