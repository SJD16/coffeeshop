from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.http import HttpResponse
from django.db.models import Sum, Count

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

def delete_ingredient(request, item_id):
    #ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    ingredient = Ingredient.objects.filter(id=item_id)
    ingredient.delete()
    messages.success(request, "Ingredient deleted successfully!")
    return redirect('ingredients')

def purchase_item(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)

    # Check inventory availability
    requirements = RecipeRequirement.objects.filter(menu_item=item)
    for req in requirements:
        if req.ingredient.quantity_available < req.quantity:
            messages.error(request, f"Not enough {req.ingredient.name} in stock to make {item.name}.")
            return redirect('menu_items')

    # Log the purchase
    Purchase.objects.create(menu_item=item)

    # Update inventory
    for req in requirements:
        ingredient = req.ingredient
        ingredient.quantity_available -= req.quantity
        ingredient.save()

    # Success message
    messages.success(request, f"✅ You purchased {item.name} successfully!")

    # Redirect to log (prevents duplicate on refresh)    
    return redirect('purchase_confirmation', item_id=item.id)

def purchase_confirmation(request, item_id):
    item2 = MenuItem.objects.get(id=item_id)
    return render(request, 'restaurant/purchase.html', {'item': item2})
    

def log_view(request):
    purchases = Purchase.objects.all().order_by('-timestamp')
    return render(request, 'restaurant/log.html', {'purchases': purchases})

def recipe_view(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    requirements = RecipeRequirement.objects.filter(menu_item=item)

    return render(request, 'restaurant/recipe.html', {'item': item, 'requirements': requirements})



def revenue_view(request):
    purchases = Purchase.objects.select_related('menu_item')
    total_revenue = purchases.aggregate(Sum('menu_item__price'))['menu_item__price__sum'] or 0
    total_sales = purchases.count()
    return render(request, 'restaurant/revenue.html', {
        'purchases': purchases,
        'total_revenue': total_revenue,
        'total_sales': total_sales
    })

"""
Owner
view all the ingredients in the inventory
delete or add ingredients from the inventory
view the items in the menu
view the purchases made at the restaurant
view the profit and revenue for the restaurant

"""

"""
def purchase_item_v1(request, item_id):
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
    """