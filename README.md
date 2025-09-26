# Coffe Shop App With Django

Welcome to...

## What’s Inside:

   * coffeshop
   * restaurant
     [Nmap Discovery & Scanning](./1.%20Nmap%20Discovery%20&%20Scanning/metasploitable-scan.md)
   * 
   
     [Wireshark HTTP Analysis](./2.%20Wireshark%20HTTP%20Analysis/Wireshark-analysis.md)
   * DVWA (Damn Vulnerable Web App): A platform to practice common web vulnerabilities, including:
        * Command Execution
        * Cross-Site Scripting (XSS)
        * SQL Injection

## If you change the models How to check the DB
    
   *   You need to open your python shell
python manage.py shell
   *   Import your models
from restaurant.models import Ingredient, MenuItem, RecipeRequirement, Purchase
## Query data
i= Ingredient.objects.create()