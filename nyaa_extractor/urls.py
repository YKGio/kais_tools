from django.urls import path
from . import views

urlpatterns = [
    path('', views.ui, name='ui'),
    path('get_magnets/', views.get_magnets, name='get_magnets'),
]
