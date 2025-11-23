from django.db import models
from accounts.models import User
from restaurants.models import Restaurant

class Commission(models.Model):
    """Platform commission settings"""
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='commissions')
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.restaurant.name} - {self.percentage}%"

class Payout(models.Model):
    """Track payouts to restaurants and delivery partners"""
    RECIPIENT_TYPE_CHOICES = (
        ('restaurant', 'Restaurant'),
        ('delivery', 'Delivery Partner'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    
    recipient_type = models.CharField(max_length=20, choices=RECIPIENT_TYPE_CHOICES)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payouts')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.recipient.username} - ${self.amount} - {self.status}"

class Promotion(models.Model):
    """Promotions and discount codes"""
    PROMO_TYPE_CHOICES = (
        ('percentage', 'Percentage Discount'),
        ('fixed', 'Fixed Amount Discount'),
        ('free_delivery', 'Free Delivery'),
    )
    
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    promo_type = models.CharField(max_length=20, choices=PROMO_TYPE_CHOICES)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_order = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    maximum_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Validity
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    # Usage limits
    usage_limit = models.IntegerField(null=True, blank=True)
    usage_per_user = models.IntegerField(default=1)
    times_used = models.IntegerField(default=0)
    
    # Targeting
    applicable_restaurants = models.ManyToManyField(Restaurant, blank=True)
    first_order_only = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.code} - {self.promo_type}"

class PromoUsage(models.Model):
    """Track promo code usage"""
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, related_name='usages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    used_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.promotion.code} - Order {self.order.order_number}"

class LoyaltyProgram(models.Model):
    """Loyalty program settings"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    points_per_dollar = models.DecimalField(max_digits=5, decimal_places=2)
    dollars_per_point = models.DecimalField(max_digits=5, decimal_places=2)
    minimum_points_redemption = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class FraudAlert(models.Model):
    """Track potential fraud"""
    ALERT_TYPE_CHOICES = (
        ('multiple_accounts', 'Multiple Accounts'),
        ('payment_fraud', 'Payment Fraud'),
        ('fake_reviews', 'Fake Reviews'),
        ('other', 'Other'),
    )
    
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('investigating', 'Investigating'),
        ('resolved', 'Resolved'),
        ('dismissed', 'Dismissed'),
    )
    
    alert_type = models.CharField(max_length=30, choices=ALERT_TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fraud_alerts', null=True, blank=True)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_fraud_alerts')
    resolution_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.alert_type} - {self.status}"

class SupportTicket(models.Model):
    """Customer support tickets"""
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    )
    
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    )
    
    ticket_number = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_tickets')
    order = models.ForeignKey('orders.Order', on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')
    resolution = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.ticket_number} - {self.subject}"
