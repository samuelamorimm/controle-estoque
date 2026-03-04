from django.urls import include, path
from .views import ProductView

urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
    path('products/<int:pk>/', ProductView.as_view())
] 