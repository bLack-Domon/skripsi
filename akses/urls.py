from django.urls import path
from .import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('karyawan/', views.karyawan, name='karyawan'),
    path('unit/', views.unit, name='unit'),


    path('form-karyawan/', views.formkaryawan, name='formkaryawan'),
    path('input-karyawan/', views.inputkaryawan, name='inputkaryawan'),


    path('login-page/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
  
]
