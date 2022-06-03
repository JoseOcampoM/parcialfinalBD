from django.urls import path
from apps.entradas import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('create', views.create, name='create'),
]