# Getting Started with Food Delivery Application

This guide will help you set up and run the food delivery application.

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/surendra767116/node.git
cd node

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Setup

```bash
# Run migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser
```

### 3. Run the Server

```bash
python manage.py runserver
```

Visit:
- **Home page**: http://localhost:8000/
- **Admin panel**: http://localhost:8000/admin/

## Setting Up Initial Data

### 1. Create Cuisines

Login to the admin panel and add some cuisines:
- Italian
- Chinese
- Indian
- Mexican
- American
- Thai

### 2. Create Restaurants

Navigate to `Restaurants` → `Add` and create restaurants with:
- Restaurant owner (must be a user with `restaurant` type)
- Name, description, address
- Location coordinates (latitude/longitude)
- Contact information
- Opening/closing times
- Delivery settings

### 3. Add Menu Items

For each restaurant:
- Create menu categories (Appetizers, Main Course, Desserts, etc.)
- Add menu items with prices and descriptions
- Set item availability

### 4. Register Delivery Partners

Create users with `delivery` type and set up their profiles:
- Vehicle information
- License details
- Document verification status

### 5. Set Up Delivery Zones

Define service areas:
- Zone name
- Polygon coordinates (JSON format)
- Base delivery fee

### 6. Configure Promotions

Create promotional campaigns:
- Discount codes
- Discount type (percentage, fixed, free delivery)
- Validity period
- Usage limits

## User Roles

### Customer
- Browse restaurants and menus
- Place orders
- Track deliveries
- Rate and review

### Restaurant Owner
- Manage restaurant profile
- Update menu items
- Process orders
- View analytics

### Delivery Partner
- Accept delivery assignments
- Update order status
- Track earnings

### Admin
- Manage all users and entities
- Configure commissions and payouts
- Handle support tickets
- Monitor fraud alerts

## Database Models Overview

### User Management
- Custom User model with role-based access
- Extended profiles for customers and delivery partners
- Authentication and authorization

### Restaurant System
- Restaurant profiles with locations
- Menu management with categories
- Cuisine classifications
- Rating and review system

### Order Processing
- Complete order lifecycle management
- Real-time order tracking
- Multiple payment methods
- Order history and analytics

### Delivery Management
- Delivery zone configuration
- Partner assignment system
- Earnings and commission tracking
- Performance metrics

### Admin Tools
- Commission management
- Payout processing
- Promotional campaigns
- Loyalty programs
- Fraud detection
- Support ticket system

## API Development (Optional)

To expose REST APIs:

1. Create serializers in each app
2. Define ViewSets
3. Configure URL routing
4. Add authentication (JWT tokens recommended)

Example serializer:
```python
from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
```

Example ViewSet:
```python
from rest_framework import viewsets
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
```

## Production Deployment

### Environment Variables

Create a `.env` file:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### Database

Use PostgreSQL or MySQL for production:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'food_delivery',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static Files

```bash
python manage.py collectstatic
```

### Security Settings

- Set `DEBUG = False`
- Use a strong `SECRET_KEY`
- Configure `ALLOWED_HOSTS`
- Set up HTTPS
- Enable CSRF protection
- Configure secure cookies

### Web Server

Use Gunicorn with Nginx:
```bash
pip install gunicorn
gunicorn food_delivery.wsgi:application --bind 0.0.0.0:8000
```

## Troubleshooting

### Migration Issues
```bash
python manage.py makemigrations
python manage.py migrate
```

### Clear Database
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Permission Errors
Check file permissions and ensure the media directory is writable:
```bash
chmod -R 755 media/
```

## Next Steps

1. **Implement REST APIs** for mobile/web apps
2. **Add real-time features** using WebSockets (Django Channels)
3. **Integrate payment gateways** (Stripe, PayPal, etc.)
4. **Add map integration** (Google Maps API)
5. **Implement notifications** (email, SMS, push)
6. **Add analytics dashboard** for insights
7. **Create mobile apps** (React Native, Flutter)
8. **Set up CI/CD pipeline**

## Support

For issues or questions:
- Create a GitHub issue
- Check the README.md for more details
- Review the Django documentation

## License

MIT License - See LICENSE file for details
