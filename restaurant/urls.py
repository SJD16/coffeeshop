from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('inventory/', views.inventory_view, name='ingredients'),
    path('menu/', views.menu, name='menu_items'),
    path('log/', views.log_view, name='log'),
    path('purchase/<int:item_id>/', views.purchase_item, name='purchases'),
    path('recipe/<int:item_id>/', views.recipe_view, name='recipe'),
    path('purchase/confirmation/<int:item_id>/', views.purchase_confirmation, name='purchase_confirmation'),
    path('inventory/delete/<int:item_id>/', views.delete_ingredient, name='delete_ingredient'),
    path('revenue/', views.revenue_view, name='revenue_view'),
    #path('login/', views.login_view, name='login_view'),
    #re_path(r'^.*$', views.menu, name='menu'),
    #re_path(r'^(?!menu|inventory|log|purchase).*$', views.menu, name='menu'),
    #re_path(r'^(?!menu|inventory|log|purchase).*$', views.menu, name='menu'),
]