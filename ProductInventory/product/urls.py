from django.urls import path
from . import views

urlpatterns = [
    path('',views.addproduct),
    path('add/', views.addproduct, name='addproduct'),
    path('view/', views.viewproduct, name='viewproduct'),
    path('delete/<int:id>/', views.deleteproduct, name='deleteproduct'),
    path('view1/',views.showproduct_price_exceed_20000, name='viewproduct1'),
    path('update/<int:id>/',views.updateproduct,name='updateproduct'),
]