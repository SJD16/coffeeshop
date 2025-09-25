from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_available = models.FloatField()  # e.g., in grams, liters, units

    def __str__(self):
        return self.name


# Menu item (what customers can order)
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


# Recipe requirements (link menu item to ingredients)
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()  # amount of ingredient required

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} for {self.menu_item.name}"


# Purchase log
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item.name} purchased at {self.timestamp}"