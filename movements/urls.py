from django.urls import include, path
from .views import MovementView

urlpatterns = [
    path('movements/', MovementView.as_view(), name='movements'),
    path('movements/<int:pk>/', MovementView.as_view(), name='movements'),
] 