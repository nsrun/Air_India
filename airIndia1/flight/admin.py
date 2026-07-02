from django.contrib import admin
from .models import airindia_Flight, Booking, User
# Register your models here.
admin.site.register(airindia_Flight)
admin.site.register(Booking)
admin.site.register(User)