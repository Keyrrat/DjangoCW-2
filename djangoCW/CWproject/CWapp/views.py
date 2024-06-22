#KIRAT ASLAM

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Calling templates from the CWapp templates folder
def home(request):
    return render(request, 'CWapp/home.html')

def Userlogin(request):
    return render(request, 'CWapp/Userlogin.html')

def registration(request):
    return render(request, 'CWapp/registration.html')

def viewEquipment(request):
    return render(request, 'CWapp/viewEquipment.html')

def UserviewBookings(request):
    return render(request, 'CWapp/UserviewBookings.html')

def AdminViewBookings(request):
    return render(request, 'CWapp/AdminviewBookings.html')

#Calls navbar from the AppProject templates folder
def navbar(request):
    return render(request, 'navbar.html')