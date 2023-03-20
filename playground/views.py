from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.http import HttpResponse
from store.models import Product, OrderItem
# Create your views here.
# request -> response
# request handler
# action

# ORM -> Object Relational Mapper
# managers -> ORM -> QuerySet
# managers are like managers in real life they manage the data in the db interface to db
# .objects -> manager
# querysets -> ORM -> list of objects
# querysets are query results from the db
# queryset encapsulates query and executes it when needed 
# .all() -> queryset
# .filter() -> queryset
# .get() -> object
# .create() -> object
# .update() -> object

# retreiving data from db
# .all() returns all the objects in the db
# .filter() returns all the objects that match the filter
# .get() returns the first object that matches the filter
# .create() creates a new object in the db
# .update() updates an object in the db
# look up types of filters
# https://docs.djangoproject.com/en/3.1/topics/db/queries/#field-lookups
# gt -> greater than
# gte -> greater than or equal to
# lt -> less than
# lte -> less than or equal to
# complex filtering using chaining
# .filter().filter().filter()
# .filter().exclude()
# .filter().exclude().filter()
# using OR
# .filter(Q(price__gt=100) | Q(price__lt=10))
# referencing fields using F
# .filter(price__gt=F('inventory'))
# .filter(price__gt=F('inventory') * 2)
# sorting data
# .order_by('price')
# .order_by('-price')
# .order_by('price', 'inventory')
# .order_by('price', '-inventory')
# .order_by('price', '-inventory').reverse()
# earliest and latest
# .earliest('price') -> in ascending order
# .latest('price') -> in descending order
# limiting data
# .all()[:10]
# .all()[10:20]
# .all()[10:20:2]
# selecting specific fields
# .values('name', 'price')
# .values_list('name', 'price')
# .values_list('name', 'price', flat=True)
# .values_list('name', 'price', named=True)
# .values_list('name', 'price', named=True).first()

def say_hello(request):
    # pull data from db
    # Transform
    # send email
    # try:
    #     prodcut = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    queryset = Product.objects.filter(
        id__in = OrderItem.objects.values('product__id').distinct()).order_by(
        'title')
    # queryset = OrderItem.objects.values('product__id').distinct()

    # return HttpResponse('Hello World')
    return render(request, 'hello.html', { 'name': 'Awais', 'products': list(queryset) })