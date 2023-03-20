from django.shortcuts import render
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

def say_hello(request):
    # pull data from db
    # Transform
    # send email
    query_set = Product.objects.all()
    for product in query_set:
        print(product)
    return render(request, 'hello.html', { 'name': 'Awais' })