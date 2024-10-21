
# Register your models here.
from django.contrib import admin
from .models import Donor, BloodType, BloodBank, Request

admin.site.register(Donor)
admin.site.register(BloodType)
admin.site.register(BloodBank)
admin.site.register(Request)
