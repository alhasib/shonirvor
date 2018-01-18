# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import ProfileForm
from django.shortcuts import render, redirect
from .models import Division, District, Area, Profile
#from django.shortcuts import render

def create_profile(request):
    if request.method=='POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #profile.user = request.user
            return redirect('edit')
            #return redirect('edit')
    else:
        form = ProfileForm()
        return render(request,'profile/create_profile.html',{'form':form})

def profile_detail(request):
    #print("hasib")
    try:
        pro = Profile.objects.get(full_name="jaman")
        print("hasib")
        context = {'profile':pro}
    except:
        context = {'errmsg':"You have no profile to show"}
    return render(request,'profile/profile_detail.html', context)


def edit_profile(request):
    profile = Profile.objects.get(full_name="shuvro")
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance = profile)
        if form.is_valid():
            profile = form.save()
            #profile.user = request.user
            profile.save()
            return render(request,'profile/profile.html',{'form':form})

    else:
        form = ProfileForm(instance=profile)
        return render(request,'profile/profile.html',{'form':form})
