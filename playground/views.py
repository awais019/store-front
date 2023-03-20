from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse
from store.models import Product
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

def say_hello(request):
    # pull data from db
    # Transform
    # send email
    # try:
    #     prodcut = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass

    queryset = Product.objects.filter(Q(inventory__lt=10) | Q(price__lt=20))

    # return HttpResponse('Hello World')
    return render(request, 'hello.html', { 'name': 'Awais', 'products': list(queryset) })