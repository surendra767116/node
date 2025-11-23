from django.contrib import admin
from .models import DeliveryZone, DeliveryAssignment, DeliveryEarnings

@admin.register(DeliveryZone)
class DeliveryZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_delivery_fee', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(DeliveryAssignment)
class DeliveryAssignmentAdmin(admin.ModelAdmin):
    list_display = ('order', 'delivery_partner', 'status', 'assigned_at')
    list_filter = ('status', 'assigned_at')
    search_fields = ('order__order_number', 'delivery_partner__username')

@admin.register(DeliveryEarnings)
class DeliveryEarningsAdmin(admin.ModelAdmin):
    list_display = ('delivery_partner', 'order', 'total', 'net_earning', 'paid', 'created_at')
    list_filter = ('paid', 'created_at')
    search_fields = ('delivery_partner__username', 'order__order_number')
