from django.urls import include, path
from .views import CategoryView

urlpatterns = [
    path('categorys/', CategoryView.as_view(), name='categorys'),
    path('categorys/<int:pk>/', CategoryView.as_view())
] 