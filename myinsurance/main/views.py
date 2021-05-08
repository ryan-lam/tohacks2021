from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

# Create your views here.

# Create the login form
class Login(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput)



# Login page (FULLY WORKS)
def index(request):
    if request.method == "POST":
        login = Login(request.POST)
        if login.is_valid():
            username =  login.cleaned_data["username"]
            password =  login.cleaned_data["password"]

            if username == "rep" and password == "1234":
                request.session["user"] = username
                request.session["type"] = "rep"
                return HttpResponseRedirect(reverse("repdashboard"))
            elif username == "client" and password == "1234":
                request.session["user"] = username
                request.session["type"] = "client"
                return HttpResponseRedirect(reverse("clientdashboard"))
            else:
                request.session.flush()
                return render (request, "index.html", {
                    "login":Login(), "attempt":True
                })
    else:
        request.session.flush()
        return render(request, "index.html", {
            "login": Login(), "attempt":False
    })



def repdashboard(request):
    if "user" in request.session and request.session["type"] == "rep":
        return render(request, "repdashboard.html")
    else:
        return HttpResponseRedirect(reverse("index"))


def clientdashboard(request):
    if "user" in request.session and request.session["type"] == "client":
        return render(request, "clientdashboard.html")
    else:
        return HttpResponseRedirect(reverse("index"))


