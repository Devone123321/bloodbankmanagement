
# Register your models here.
from django.contrib import admin
from .models import Donor, BloodType, BloodBank, Request

class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'blood_type', 'last_donation', 'contact_number')
    search_fields = ('name', 'contact_number')

class RequestAdmin(admin.ModelAdmin):
    list_display = ('recipient_name', 'blood_type', 'quantity_needed', 'request_date')
    search_fields = ('recipient_name', 'blood_type')

class StockAdmin(admin.ModelAdmin):
    list_display = ('blood_type','quantity_in_units')
    search_fields = ('blood_type','quantity_in_units')

admin.site.register(Donor, DonorAdmin)
admin.site.register(BloodType)
admin.site.register(BloodBank,StockAdmin)
admin.site.register(Request, RequestAdmin)
