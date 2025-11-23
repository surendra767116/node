from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import User, CustomerProfile, DeliveryPartnerProfile

def home(request):
    """Home page view"""
    return render(request, 'home.html', {
        'title': 'Food Delivery App - Home'
    })

def restaurants(request):
    """Restaurants listing page"""
    return render(request, 'restaurants.html')

def restaurant_detail(request, restaurant_id):
    """Restaurant detail and menu page"""
    return render(request, 'restaurant_detail.html', {
        'restaurant_id': restaurant_id
    })

def cart(request):
    """Shopping cart page"""
    return render(request, 'cart.html')

def orders(request):
    """Orders listing and tracking page"""
    return render(request, 'orders.html')

def profile(request):
    """User profile page"""
    return render(request, 'profile.html')

@api_view(['POST'])
def register_user(request):
    """API endpoint for user registration"""
    # Implementation for user registration
    return JsonResponse({'message': 'Registration endpoint - to be implemented'})

@api_view(['POST'])
def login_user(request):
    """API endpoint for user login"""
    # Implementation for user login
    return JsonResponse({'message': 'Login endpoint - to be implemented'})

@api_view(['POST'])
@login_required
def logout_user(request):
    """API endpoint for user logout"""
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'})

@api_view(['GET'])
@login_required
def user_profile(request):
    """API endpoint for user profile"""
    user = request.user
    profile_data = {
        'username': user.username,
        'email': user.email,
        'user_type': user.user_type,
        'phone': user.phone,
    }
    return JsonResponse(profile_data)
