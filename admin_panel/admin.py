from django.contrib import admin
from .models import Commission, Payout, Promotion, PromoUsage, LoyaltyProgram, FraudAlert, SupportTicket

@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'percentage', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active', 'start_date')
    search_fields = ('restaurant__name',)

@admin.register(Payout)
class PayoutAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'recipient_type', 'amount', 'status', 'created_at')
    list_filter = ('recipient_type', 'status', 'created_at')
    search_fields = ('recipient__username', 'transaction_id')

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('code', 'promo_type', 'discount_value', 'is_active', 'start_date', 'end_date', 'times_used')
    list_filter = ('promo_type', 'is_active', 'start_date')
    search_fields = ('code', 'description')

@admin.register(PromoUsage)
class PromoUsageAdmin(admin.ModelAdmin):
    list_display = ('promotion', 'user', 'order', 'discount_amount', 'used_at')
    list_filter = ('used_at',)
    search_fields = ('promotion__code', 'user__username', 'order__order_number')

@admin.register(LoyaltyProgram)
class LoyaltyProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'points_per_dollar', 'dollars_per_point', 'is_active')
    list_filter = ('is_active',)

@admin.register(FraudAlert)
class FraudAlertAdmin(admin.ModelAdmin):
    list_display = ('alert_type', 'user', 'status', 'assigned_to', 'created_at')
    list_filter = ('alert_type', 'status', 'created_at')
    search_fields = ('user__username', 'description')

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'user', 'subject', 'priority', 'status', 'assigned_to', 'created_at')
    list_filter = ('priority', 'status', 'created_at')
    search_fields = ('ticket_number', 'user__username', 'subject')
