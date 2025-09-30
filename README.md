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

To upload the data to the DB from Json files use:
python manage.py loaddata ingredients.json
python manage.py loaddata menuitems.json
python manage.py loaddata reciperequirements.json


To generate a relation graphic of the DB
install 
 pip install django-extensions  
 pip install pydotplus           
 and on settings.py add on "INSTALLED_APPS"

 'django_extensions',

 then run 

 python manage.py graph_models -a -g -o myapp_models.dot

 then use: 
 dreampuf.github.io/GraphvizOnline

 to display it