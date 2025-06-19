from django.contrib import admin

from cleaning.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'address', 'phone', 'date', 'service', 'payment', 'status', 'cancel_reason')
    list_editable = ('status', 'cancel_reason')

