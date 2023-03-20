from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('collections/', views.CollectionList.as_view(), name='collection_list'),
    path('collections/<int:pk>/', views.CollectionDetails.as_view(), name='collection_detail'),
]