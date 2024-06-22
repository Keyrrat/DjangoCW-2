#KIRAT ASLAM

from . import views
from django.urls import path


urlpatterns = [
    path('', views.home),
    path('Userlogin/', views.Userlogin),
    path('registration/', views.registration),
    path('viewEquipment/', views.viewEquipment),
    path('UserviewBookings/', views.UserviewBookings),
    path('AdminViewBookings/', views.AdminViewBookings),
    path('navbar/', views.navbar)
]
