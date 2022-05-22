from django.urls import path
from products.api.viewset import ProductDetailAPIView, ProductsListAPIView
urlpatterns = [
    path('api/v1/products-list', ProductsListAPIView.as_view(), name='things_list'),
    path('api/v1/<int:pk>', ProductDetailAPIView.as_view(), name='thing_detail'),

]
