from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to the CoffeeShop!")

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'restaurant/menu.html', {'menu_items': items})


#we take all ingredients from the database and pass them ('ingredients') to the template
def inventory_view(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'restaurant/inventory.html', {'ingredients': ingredients})

def purchase_item(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    # Log the purchase
    Purchase.objects.create(menu_item=item)
    # Update inventory
    requirements = RecipeRequirement.objects.filter(menu_item=item)
    for req in requirements:
        ingredient = req.ingredient
        ingredient.quantity_available -= req.quantity
        ingredient.save()
    return render(request, 'restaurant/purchase.html', {'item': item})


def log_view(request):
    purchases = Purchase.objects.all().order_by('-timestamp')
    return render(request, 'restaurant/log.html', {'purchases': purchases})

def recipe_view(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    requirements = RecipeRequirement.objects.filter(menu_item=item)

    return render(request, 'restaurant/recipe.html', {'item': item, 'requirements': requirements})


"""
Owner
view all the ingredients in the inventory
delete or add ingredients from the inventory
view the items in the menu
view the purchases made at the restaurant
view the profit and revenue for the restaurant

"""