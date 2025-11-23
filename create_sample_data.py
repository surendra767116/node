#!/usr/bin/env python
"""
Script to create sample data for the food delivery application.
Run this after setting up the database and creating a superuser.

Usage: python create_sample_data.py
"""

import os
import django
import sys

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_delivery.settings')
django.setup()

from django.contrib.auth import get_user_model
from accounts.models import CustomerProfile, DeliveryPartnerProfile
from restaurants.models import Restaurant, Cuisine, MenuCategory, MenuItem
from datetime import time

User = get_user_model()

def create_sample_data():
    print("Creating sample data for Food Delivery Application...")
    
    # Create cuisines
    print("\n1. Creating cuisines...")
    cuisines_data = ['Italian', 'Chinese', 'Indian', 'Mexican', 'American', 'Thai', 'Japanese']
    cuisines = {}
    for cuisine_name in cuisines_data:
        cuisine, created = Cuisine.objects.get_or_create(name=cuisine_name)
        cuisines[cuisine_name] = cuisine
        if created:
            print(f"   ✓ Created cuisine: {cuisine_name}")
        else:
            print(f"   - Cuisine already exists: {cuisine_name}")
    
    # Create sample restaurant owner
    print("\n2. Creating restaurant owner...")
    owner, created = User.objects.get_or_create(
        username='restaurant_owner',
        defaults={
            'email': 'owner@restaurant.com',
            'user_type': 'restaurant',
            'phone': '1234567890',
            'address': '123 Main St, City',
            'is_verified': True
        }
    )
    if created:
        owner.set_password('password123')
        owner.save()
        print("   ✓ Created restaurant owner (username: restaurant_owner, password: password123)")
    else:
        print("   - Restaurant owner already exists")
    
    # Create sample restaurant
    print("\n3. Creating sample restaurant...")
    restaurant, created = Restaurant.objects.get_or_create(
        name='Delicious Bites',
        defaults={
            'owner': owner,
            'description': 'Best food in town with a variety of cuisines',
            'address': '456 Food Street, Downtown',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'phone': '1234567890',
            'email': 'contact@deliciousbites.com',
            'license_number': 'REST123456',
            'is_verified': True,
            'opening_time': time(9, 0),
            'closing_time': time(22, 0),
            'delivery_time': 30,
            'minimum_order': 10.00,
            'delivery_fee': 3.50,
            'rating': 4.5
        }
    )
    if created:
        print("   ✓ Created restaurant: Delicious Bites")
    else:
        print("   - Restaurant already exists")
    
    # Create menu categories
    print("\n4. Creating menu categories...")
    categories_data = ['Appetizers', 'Main Course', 'Desserts', 'Beverages']
    categories = {}
    for idx, cat_name in enumerate(categories_data):
        category, created = MenuCategory.objects.get_or_create(
            restaurant=restaurant,
            name=cat_name,
            defaults={'display_order': idx}
        )
        categories[cat_name] = category
        if created:
            print(f"   ✓ Created category: {cat_name}")
        else:
            print(f"   - Category already exists: {cat_name}")
    
    # Create sample menu items
    print("\n5. Creating sample menu items...")
    menu_items_data = [
        {
            'category': 'Appetizers',
            'name': 'Spring Rolls',
            'description': 'Crispy vegetable spring rolls served with sweet chili sauce',
            'price': 6.99,
            'item_type': 'veg',
            'preparation_time': 15
        },
        {
            'category': 'Main Course',
            'name': 'Margherita Pizza',
            'description': 'Classic Italian pizza with fresh mozzarella and basil',
            'price': 12.99,
            'item_type': 'veg',
            'preparation_time': 20
        },
        {
            'category': 'Main Course',
            'name': 'Chicken Biryani',
            'description': 'Aromatic basmati rice with tender chicken and spices',
            'price': 14.99,
            'item_type': 'non_veg',
            'preparation_time': 25
        },
        {
            'category': 'Desserts',
            'name': 'Chocolate Lava Cake',
            'description': 'Warm chocolate cake with molten center',
            'price': 5.99,
            'item_type': 'veg',
            'preparation_time': 10
        },
        {
            'category': 'Beverages',
            'name': 'Fresh Lime Soda',
            'description': 'Refreshing lime soda with a hint of mint',
            'price': 3.49,
            'item_type': 'veg',
            'preparation_time': 5
        }
    ]
    
    for item_data in menu_items_data:
        item, created = MenuItem.objects.get_or_create(
            restaurant=restaurant,
            name=item_data['name'],
            defaults={
                'category': categories[item_data['category']],
                'description': item_data['description'],
                'price': item_data['price'],
                'item_type': item_data['item_type'],
                'preparation_time': item_data['preparation_time'],
                'rating': 4.2
            }
        )
        if created:
            print(f"   ✓ Created menu item: {item_data['name']}")
        else:
            print(f"   - Menu item already exists: {item_data['name']}")
    
    # Create sample customer
    print("\n6. Creating sample customer...")
    customer, created = User.objects.get_or_create(
        username='customer1',
        defaults={
            'email': 'customer@example.com',
            'user_type': 'customer',
            'phone': '9876543210',
            'address': '789 Customer Ave, Suburb',
            'is_verified': True
        }
    )
    if created:
        customer.set_password('password123')
        customer.save()
        CustomerProfile.objects.create(user=customer, loyalty_points=100)
        print("   ✓ Created customer (username: customer1, password: password123)")
    else:
        print("   - Customer already exists")
    
    # Create sample delivery partner
    print("\n7. Creating sample delivery partner...")
    delivery_partner, created = User.objects.get_or_create(
        username='delivery1',
        defaults={
            'email': 'delivery@example.com',
            'user_type': 'delivery',
            'phone': '5555555555',
            'address': '321 Delivery Road, City',
            'is_verified': True
        }
    )
    if created:
        delivery_partner.set_password('password123')
        delivery_partner.save()
        DeliveryPartnerProfile.objects.create(
            user=delivery_partner,
            vehicle_type='Motorcycle',
            vehicle_number='ABC1234',
            license_number='DL123456789',
            document_verified=True,
            status='available',
            rating=4.8
        )
        print("   ✓ Created delivery partner (username: delivery1, password: password123)")
    else:
        print("   - Delivery partner already exists")
    
    print("\n" + "="*60)
    print("Sample data creation completed!")
    print("="*60)
    print("\nLogin credentials:")
    print("  Restaurant Owner: restaurant_owner / password123")
    print("  Customer: customer1 / password123")
    print("  Delivery Partner: delivery1 / password123")
    print("\nAdmin panel: http://localhost:8000/admin/")
    print("="*60)

if __name__ == '__main__':
    try:
        create_sample_data()
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)
