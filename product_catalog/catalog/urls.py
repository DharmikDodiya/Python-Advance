# Using @router decorator with class-based views (CBVs)

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('products/', views.list_products, name='list_products'),
#     path('products/create', views.create_product, name='create_product'),
#     path('products/<int:pk>', views.retrieve_product, name='retrieve_product'),
#     path('products/update/<int:pk>', views.update_product, name='update_product'),
#     path('products/delete/<int:pk>', views.delete_product, name='delete_product'),
# ]

# Using ModelViewSet

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
