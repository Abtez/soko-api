from .views import AllProductsViews
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('products/', AllProductsViews.as_view()),
    path('products/<slug:uuid>', AllProductsViews.as_view()),
    # path('products/<int:uuid>', views.product_detail)
]