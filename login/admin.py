from django.contrib import admin
from login.models import Customer, Admin
from booking.models import Contact,Storages,Booking
# Register your models here.
admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Contact)
admin.site.register(Storages)
admin.site.register(Booking)