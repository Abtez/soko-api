from .views import AllProductsViews,VendorProfileViews, UserViews
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('products/', AllProductsViews.as_view()),
    path('products/<slug:uuid>', AllProductsViews.as_view()),
    
    path('profiles/', VendorProfileViews.as_view()),
    path('profiles/<slug:user>', VendorProfileViews.as_view()),
    
    path('users/', UserViews.as_view()),
    path('users/<int:id>', UserViews.as_view()),
]