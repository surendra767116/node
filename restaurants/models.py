from django.db import models
from accounts.models import User

class Restaurant(models.Model):
    """Restaurant model"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_restaurants')
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='restaurants/logos/', null=True, blank=True)
    banner_image = models.ImageField(upload_to='restaurants/banners/', null=True, blank=True)
    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    
    # Business details
    license_number = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Ratings and reviews
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    total_reviews = models.IntegerField(default=0)
    
    # Operational details
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    delivery_time = models.IntegerField(help_text="Average delivery time in minutes")
    minimum_order = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Cuisine(models.Model):
    """Cuisine types"""
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class RestaurantCuisine(models.Model):
    """Restaurant-Cuisine relationship"""
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='cuisines')
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('restaurant', 'cuisine')
    
    def __str__(self):
        return f"{self.restaurant.name} - {self.cuisine.name}"

class MenuCategory(models.Model):
    """Menu categories for organizing items"""
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_categories')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    display_order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['display_order', 'name']
        verbose_name_plural = "Menu Categories"
    
    def __str__(self):
        return f"{self.restaurant.name} - {self.name}"

class MenuItem(models.Model):
    """Menu items"""
    ITEM_TYPE_CHOICES = (
        ('veg', 'Vegetarian'),
        ('non_veg', 'Non-Vegetarian'),
        ('vegan', 'Vegan'),
    )
    
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    category = models.ForeignKey(MenuCategory, on_delete=models.SET_NULL, null=True, related_name='items')
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_items/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_type = models.CharField(max_length=10, choices=ITEM_TYPE_CHOICES)
    is_available = models.BooleanField(default=True)
    preparation_time = models.IntegerField(help_text="Preparation time in minutes")
    
    # Ratings
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    total_reviews = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.restaurant.name} - {self.name}"

class RestaurantReview(models.Model):
    """Reviews for restaurants"""
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    order = models.ForeignKey('orders.Order', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('restaurant', 'user', 'order')
    
    def __str__(self):
        return f"{self.user.username} - {self.restaurant.name} - {self.rating}★"
