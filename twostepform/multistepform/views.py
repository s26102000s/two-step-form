from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import MultiStepFormModel

# Create your views here.
def multistepformexample(request):
    return render(request,"multistepformexample.html")

def multistepformexample_save(request):
    if request.method!="POST":
        return render(request,"multistepformexample.html")
    else:
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        phone=request.POST.get("phone")
        father=request.POST.get("father")
        marrital=request.POST.get("marrital")
        gender=request.POST.get("gender")
        email=request.POST.get("email")
        spouse=request.POST.get("spouse")

        try:
            multistepform=MultiStepFormModel(fname=fname,lname=lname,phone=phone,gender=gender,marrital=marrital,father=father,email=email,spouse=spouse)
            multistepform.save()
            messages.success(request,"Data Save Successfully")
            return HttpResponseRedirect(reverse('multistepformexample'))
        except:
            messages.error(request,"Error in Saving Data")
            return HttpResponseRedirect(reverse('multistepformexample'))
