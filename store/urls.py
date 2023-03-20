from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:id>/', views.ProductDetail.as_view(), name='product_detail'),
    path('collections/', views.CollectionList.as_view(), name='collection_list'),
    path('collections/<int:pk>/', views.collection_detail, name='collection_detail'),
]