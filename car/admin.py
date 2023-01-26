from django.contrib import admin

# Register your models here.
from .models import Car,Reservation


admin.site.register(Car)
admin.site.register(Reservation)