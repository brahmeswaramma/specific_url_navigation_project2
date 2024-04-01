from django.urls import path
from product.views import *
app_name='anything'
urlpatterns=[
    path('product_list/',product_list,name='product_list')
]