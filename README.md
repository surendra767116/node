# Food Delivery Application

A comprehensive Django-based food delivery platform with separate interfaces for Customers, Restaurants, Delivery Partners, and Admins.

## 🚀 Features

### User App (Customers)
- Account creation & login (email, phone, social login support)
- Browse restaurants & menus
- Search & filter (by cuisine, price, ratings, distance)
- Add to cart & place orders
- Real-time order tracking (status updates, delivery location)
- Payment integration support (UPI, cards, wallets, COD)
- Ratings & reviews for restaurants and delivery partners

### Restaurant App / Dashboard
- Restaurant registration & profile management
- Menu management (add/update items, prices, availability)
- Order management (accept/reject, update status)
- Analytics (sales reports, customer feedback)

### Delivery Partner App
- Registration & verification (documents, background check)
- Order assignment & acceptance
- Navigation & route optimization support
- Earnings tracking

### Admin Panel
- Manage users, restaurants, delivery partners
- Commission & payout management
- Promotions, discounts, and loyalty programs
- Fraud detection & customer support tools

## 📋 Requirements

- Python 3.8+
- Django 5.2.8
- SQLite (default) or PostgreSQL/MySQL for production

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/surendra767116/node.git
cd node
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application:
- Main site: http://localhost:8000/
- Admin panel: http://localhost:8000/admin/

## 📦 Project Structure

```
food_delivery/
├── accounts/           # User authentication and profiles
│   ├── models.py      # User, CustomerProfile, DeliveryPartnerProfile
│   └── admin.py       # Admin configuration
├── restaurants/        # Restaurant and menu management
│   ├── models.py      # Restaurant, MenuItem, MenuCategory, Cuisine, Reviews
│   └── admin.py       # Admin configuration
├── orders/            # Order processing and tracking
│   ├── models.py      # Order, OrderItem, OrderTracking, DeliveryReview
│   └── admin.py       # Admin configuration
├── delivery/          # Delivery management
│   ├── models.py      # DeliveryZone, DeliveryAssignment, DeliveryEarnings
│   └── admin.py       # Admin configuration
├── admin_panel/       # Admin operations
│   ├── models.py      # Commission, Payout, Promotion, FraudAlert, SupportTicket
│   └── admin.py       # Admin configuration
└── food_delivery/     # Project settings
    ├── settings.py    # Django settings
    └── urls.py        # URL configuration
```

## 🗄️ Database Models

### Accounts App
- **User**: Custom user model with support for customers, restaurant owners, delivery partners, and admins
- **CustomerProfile**: Extended customer information with loyalty points
- **DeliveryPartnerProfile**: Delivery partner details, vehicle info, and earnings

### Restaurants App
- **Restaurant**: Restaurant information and operational details
- **Cuisine**: Available cuisine types
- **MenuCategory**: Menu organization
- **MenuItem**: Individual menu items with pricing and availability
- **RestaurantReview**: Customer reviews and ratings

### Orders App
- **Order**: Complete order information and status
- **OrderItem**: Individual items in an order
- **OrderTracking**: Real-time order tracking history
- **DeliveryReview**: Delivery partner ratings

### Delivery App
- **DeliveryZone**: Service areas and delivery fees
- **DeliveryAssignment**: Order assignments to delivery partners
- **DeliveryEarnings**: Partner earnings and commission tracking

### Admin Panel App
- **Commission**: Platform commission settings per restaurant
- **Payout**: Payment tracking for restaurants and delivery partners
- **Promotion**: Discount codes and promotional campaigns
- **PromoUsage**: Promo code usage tracking
- **LoyaltyProgram**: Loyalty program configuration
- **FraudAlert**: Fraud detection and monitoring
- **SupportTicket**: Customer support ticket system

## 🔐 User Types

1. **Customer**: Browse, order, track deliveries
2. **Restaurant Owner**: Manage restaurant, menu, and orders
3. **Delivery Partner**: Accept and complete deliveries
4. **Admin**: Full system management and oversight

## 🎯 Key Functionalities

### Order Flow
1. Customer browses restaurants and adds items to cart
2. Customer places order with delivery address and payment method
3. Restaurant receives and confirms the order
4. Order is assigned to a delivery partner
5. Delivery partner picks up and delivers the order
6. Customer can track order in real-time
7. Post-delivery reviews and ratings

### Payment Support
- Cash on Delivery (COD)
- UPI
- Credit/Debit Cards
- Digital Wallets

### Admin Operations
- Monitor all orders and transactions
- Manage commissions and payouts
- Create and manage promotional campaigns
- Handle fraud alerts and support tickets
- View analytics and reports

## 🚦 Getting Started with Data

After setting up the project, you can:

1. Create cuisines through the admin panel
2. Add restaurants with menu items
3. Create customer accounts
4. Register delivery partners
5. Set up delivery zones
6. Configure promotions and loyalty programs

## 🔄 API Development (Next Steps)

To add REST API endpoints:

1. Create serializers in each app
2. Create ViewSets for each model
3. Configure URL routing in urls.py
4. Add authentication tokens

## 📝 Notes

- This is a development setup using SQLite database
- For production, configure PostgreSQL or MySQL
- Set up proper SECRET_KEY and security settings
- Configure email backend for notifications
- Add payment gateway integrations
- Implement real-time tracking with WebSockets
- Add map integration for location services

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.
