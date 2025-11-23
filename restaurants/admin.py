from django.contrib import admin
from .models import Restaurant, Cuisine, RestaurantCuisine, MenuCategory, MenuItem, RestaurantReview

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'is_verified', 'is_active', 'rating', 'created_at')
    list_filter = ('is_verified', 'is_active', 'created_at')
    search_fields = ('name', 'owner__username', 'email', 'phone')

@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(RestaurantCuisine)
class RestaurantCuisineAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'cuisine')
    list_filter = ('cuisine',)

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'display_order')
    list_filter = ('restaurant',)
    search_fields = ('name', 'restaurant__name')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'category', 'price', 'item_type', 'is_available', 'rating')
    list_filter = ('item_type', 'is_available', 'restaurant')
    search_fields = ('name', 'restaurant__name')

@admin.register(RestaurantReview)
class RestaurantReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('restaurant__name', 'user__username')
