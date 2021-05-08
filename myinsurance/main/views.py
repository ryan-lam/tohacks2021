from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Create your views here.

# Create the login form
class Login(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput)



# Login page (FULLY WORKS)
def index(request):
    if request.method == "POST":
        login = Login(request.POST)
        username =  request.POST["username"]
        password =  request.POST["password"]

        if username == "rep" and password == "1234":
            return render(request, "repdashboard.html")
        elif username == "client" and password == "1234":
            return render(request, "clientdashboard.html")
        else:
            return render (request, "index.html", {"attempt":True})

    return render(request, "index.html", {"attempt":False})

