from django.urls import path
from . import views

urlpatterns = [
    path('',views.addcustomer),
    path('add/', views.addcustomer, name='addcustomer'),
    path('view/', views.viewcustomer, name='viewcustomer'),
    path('delete/<str:email>/', views.deletecustomer, name='deletecustomer'),
]