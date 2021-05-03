from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demoPage(requset):
    return HttpResponse("Demo")

def demoPageTemplate(requset):
    return render(requset, "demo.html")


def adminLogin(request):
    return render(request,"admin_templates/signin.html")