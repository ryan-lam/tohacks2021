from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("repdashboard", views.repdashboard, name="repdashboard"),
    path("clientdashboard", views.clientdashboard, name="clientdashboard"),
]
