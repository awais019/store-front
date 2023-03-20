from django.shortcuts import render
from django.db import connection
from store.models import Order, OrderItem, Product, Customer, Collection

def say_hello(request):
    
    # queryset = Product.objects.raw("SELECT * from store_product")
    with connection.cursor() as cursor:
        cursor.execute()

    return render(request, 'hello.html', { 'name': 'Awais' })