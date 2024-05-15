from django.contrib import admin

from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product', 'closed', 'created_at')
    list_filter = ('product', 'closed')
