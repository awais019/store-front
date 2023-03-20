from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Order, OrderItem, Product, Customer, Collection

def say_hello(request):
    
    collection = Collection(pk = 1)
    collection.delete()

    # Collection.objects.filter(id__gt = 5).delete()

    return render(request, 'hello.html', { 'name': 'Awais' })