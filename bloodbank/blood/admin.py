
# Register your models here.
from django.contrib import admin
from .models import Donor, BloodType, BloodBank, Request

class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'blood_type', 'last_donation', 'contact_number')
    search_fields = ('name', 'contact_number')

admin.site.register(Donor, DonorAdmin)
admin.site.register(BloodType)
admin.site.register(BloodBank)
admin.site.register(Request)
