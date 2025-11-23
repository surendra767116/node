from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, CustomerProfile, DeliveryPartnerProfile

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'user_type', 'phone', 'is_verified', 'created_at')
    list_filter = ('user_type', 'is_verified', 'is_staff')
    search_fields = ('username', 'email', 'phone')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('user_type', 'phone', 'profile_picture', 'address', 'latitude', 'longitude', 'is_verified')}),
    )

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'loyalty_points')
    search_fields = ('user__username', 'user__email')

@admin.register(DeliveryPartnerProfile)
class DeliveryPartnerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle_type', 'status', 'document_verified', 'rating', 'total_deliveries', 'total_earnings')
    list_filter = ('status', 'document_verified', 'vehicle_type')
    search_fields = ('user__username', 'vehicle_number', 'license_number')
