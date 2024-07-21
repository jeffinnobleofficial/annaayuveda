from django.http import  JsonResponse
from django.shortcuts import redirect, render
from home.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json

from .models import products
from .models import appointments
# Create your views here.
def index(request):
    return render(request,'index.html')
def login_page(request):
    return render(request,'login.html')
def about(request):
    return render(request,'about.html')

def productss(request):
    dict_pro={
        'productss': products.objects.all()
    }   
    return render(request,'products.html',dict_pro)
  
def appointment(request):
      dict_appo={
        'appo': appointments.objects.all()
      }
      return render(request,'appointment.html', dict_appo)
  
def contact(request):
    return render(request,'contact.html')

def book_view(request):
    return render(request, 'book.html')
 
def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")
 
 
def login_page(request):
  if request.user.is_authenticated:
    
    return redirect("/")
  else:
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request,user)
        
        return redirect("/")
      else:
       
        return redirect("/login")
    return render(request,"login.html")
 
def register(request):
  form=CustomUserForm()
  if request.method=='POST':
    form=CustomUserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"Registration Success You can Login Now..!")
      return redirect('/login')
  return render(request,"register.html",{'form':form})
 
 