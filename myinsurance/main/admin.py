from django.contrib import admin

from .models import Client, Rep, Appointments

# Register your models here.

admin.site.register(Client)
admin.site.register(Rep)
admin.site.register(Appointments)