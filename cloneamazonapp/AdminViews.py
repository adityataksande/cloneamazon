from django.shortcuts import render

def admin_home(requset):
    return render (requset,"admin_templates/home.html")