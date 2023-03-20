from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer
# Create your views here.

class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer
    
    def get_serializer_context(self):
        return {'request': self.request }


class ProductDetail(APIView):
    def get(self, request, id):
        product = get_list_or_404(Product, pk=id)
        serializer = ProductSerializer(product, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request, id):
        product = get_list_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        product = get_list_or_404(Product, pk=id)
        if product.orderitems.count() > 0:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.annotate(
        products_count = Count('products')
    ).all()
    serializer_class = CollectionSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, pk):
    collection = get_list_or_404(
        Collection.objects.annotate(
        products_count = Count('products')
        ), pk = pk)
    if request.method == 'GET':
        serializer = CollectionSerializer(collection, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    elif request.method == 'DELETE':
        if collection.products.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it is associated with a product'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
