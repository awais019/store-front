from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Order, OrderItem, Product, Customer, Collection

def say_hello(request):
    
    # collection = Collection.objects.get(pk=1)
    # collection.featured_product = None
    # collection.save()

    Collection.objects.filter(pk = 1).update(featured_product = None)

    return render(request, 'hello.html', { 'name': 'Awais' })