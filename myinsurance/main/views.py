from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import Client, Rep, Profile, Appointments

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

        if (username == "rep1" or username == "rep2") and password == "1234":
            request.session["user"] = username
            request.session["type"] = "rep"
            return HttpResponseRedirect(reverse("repdashboard"))
        elif (username == "client1" or username == "client2") and password == "1234":
            request.session["user"] = username
            request.session["type"] = "client"
            return HttpResponseRedirect(reverse("clientdashboard"))
        else:
            request.session.flush()
            return render (request, "index.html", {"attempt":True})
    else:
        request.session.flush()
        return render(request, "index.html", {"attempt":False})



def repdashboard(request):
    if "user" in request.session and request.session["type"] == "rep":
        return render(request, "repdashboard.html", {
            "appointmentdb": Appointments.objects.filter(rep__username=request.session["user"]),
            "userinfo": Rep.objects.get(username=request.session["user"])
        })
    else:
        return HttpResponseRedirect(reverse("index"))


def clientdashboard(request):
    if "user" in request.session and request.session["type"] == "client":
        return render(request, "clientdashboard.html", {
            "appointmentdb": Appointments.objects.filter(client__username=request.session["user"]),
            "userinfo":Client.objects.get(username=request.session["user"])
        })
    else:
        return HttpResponseRedirect(reverse("index"))


def booking(request):
    if "user" in request.session and request.session["type"] == "client":
        return render(request, "booking.html")
    else:
        return HttpResponseRedirect(reverse("index"))


