from django.db import models
from accounts.models import User

class DeliveryZone(models.Model):
    """Delivery zones for service areas"""
    name = models.CharField(max_length=100)
    polygon_coordinates = models.JSONField(help_text="List of lat/lng coordinates defining the zone")
    is_active = models.BooleanField(default=True)
    base_delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class DeliveryAssignment(models.Model):
    """Track delivery partner assignments"""
    STATUS_CHOICES = (
        ('assigned', 'Assigned'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    )
    
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name='assignments')
    delivery_partner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delivery_assignments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='assigned')
    assigned_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(null=True, blank=True)
    rejected_at = models.DateTimeField(null=True, blank=True)
    rejection_reason = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.order.order_number} - {self.delivery_partner.username} - {self.status}"

class DeliveryEarnings(models.Model):
    """Track delivery partner earnings"""
    delivery_partner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='earnings')
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    base_fee = models.DecimalField(max_digits=10, decimal_places=2)
    distance_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tip = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2, help_text="Platform commission")
    net_earning = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.delivery_partner.username} - Order {self.order.order_number} - ${self.net_earning}"
