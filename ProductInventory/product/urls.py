from django.urls import path
from . import views

urlpatterns = [
    path('',views.addproduct),
    path('add/', views.addproduct, name='addproduct'),
    path('view/', views.viewproduct, name='viewproduct'),
    path('delete/<int:id>/', views.deleteproduct, name='deleteproduct'),
]