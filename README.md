# Coffe Shop App With Django

# ☕ CoffeeShop Management System (Django)

A Django-based web application designed to manage a coffee shop's daily operations, including menu management, inventory tracking, customer purchases, and revenue monitoring.  

---

## Features

###  User Authentication
- User login and logout using Django’s built-in authentication system
- Access control for protected views (management features)

###  Menu Management
- View all menu items
- View detailed recipes linked to each menu item
- Purchase items directly from the menu

###  Inventory Management
- View all ingredients in inventory
- Automatically update ingredient quantities after each purchase
- Delete ingredients from inventory

###  Purchase & Logs
- Log every purchase with timestamp
- View purchase history
- Prevent duplicate purchases on page refresh

###  Revenue & Profit Tracking
- View total sales
- Calculate total revenue based on menu item prices
- Display detailed purchase records

---

##  Project Structure

```text
coffeShop/
│
├── coffeeshop/            # Main project configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── restaurant/            # Core restaurant logic
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── restaurant/
│   └── ...
│
├── users/                 # Authentication (login/logout)
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── users/
│   └── ...
│
├── manage.py
└── README.md
```



##  Technologies Used

- Python 3
- Django
- SQLite (default, can be replaced with PostgreSQL/MySQL)
- HTML / CSS (Bootstrap-ready)
- Django ORM
- Django Authentication System

---

##  Installation & Setup

### 1️ Clone the repository
```bash
git clone https://github.com/your-username/coffeeShop.git
cd coffeeShop
```
### 2 Create virtual environment
```
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```
### 3 Install dependencies
```
pip install django
```

### 4 Run migrations
```
python manage.py makemigrations
python manage.py migrate
```
### 5 Create superuser
```
python manage.py createsuperuser
```
### 6 Run the server
```
python manage.py runserver
```
Open your browser and go to:
```
http://127.0.0.1:8000/
```

### Default Routes

Feature	URL
Login	/users/login/
Menu	/restaurant/menu/
Inventory	/restaurant/inventory/
Purchases	/restaurant/purchases/
Revenue	/restaurant/revenue/
Admin Panel	/admin/


## Future Improvements

* Role-based permissions (Owner vs Customer)
* Online payment integration
* Sales charts and analytics
* REST API (Django REST Framework)
* Improved UI with Bootstrap/Tailwind
* Deployment (Docker / Cloud)


## Author
Developed by SJD
Engineering & Django Project
Mexico 🇲🇽

## License
This project is for educational and portfolio purposes.


     [Wireshark HTTP Analysis](./2.%20Wireshark%20HTTP%20Analysis/Wireshark-analysis.md)
   
## extra notes
### If you change the models How to check the DB
   *   You need to open your python shell
```
python manage.py shell
```
   *   Import your models
```
from restaurant.models import Ingredient, MenuItem, RecipeRequirement, Purchase
```
## Query data
```
i= Ingredient.objects.create()
```

* To upload the data to the DB from Json files use:
```
python manage.py loaddata ingredients.json
python manage.py loaddata menuitems.json
python manage.py loaddata reciperequirements.json
```

* To generate a relation graphic of the DB install:
 ```
 pip install django-extensions  
 pip install pydotplus           
 and on settings.py add on "INSTALLED_APPS"

 'django_extensions',
```
 * then run 
```
 python manage.py graph_models -a -g -o myapp_models.dot
```
 * then use: 
 ```
 dreampuf.github.io/GraphvizOnline
```
to display it 
