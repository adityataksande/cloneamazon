from django.http.response import HttpResponse
from django. contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login


# Create your views here.
def demoPage(requset):
    return HttpResponse("Demo")

def demoPageTemplate(requset):
    return render(requset, "demo.html")


def adminLogin(request):
    return render(request,"admin_templates/signin.html")


def adminLoginProcess(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request=request, username=username, password=password)
    if user is not None:
        login(request=request, user=user)
    else:
        messages.error(request, "Error in Login! Invalid Login Credentials!")
