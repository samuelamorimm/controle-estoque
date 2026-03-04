from django.urls import include, path
from .views import SupplierView

urlpatterns = [
    path('suppliers/', SupplierView.as_view(), name='suppliers'),
    path('suppliers/<int:pk>/', SupplierView.as_view(), name='suppliers')
] 