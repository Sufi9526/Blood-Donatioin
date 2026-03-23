from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


from app1.models import *
from .forms import *
# Create your views here.



from .models import *
from app1.forms import *
def home(request):
    return render(request,'index.html')

def canyoudonate(request):
    return render(request,'canyoudonate.html')


def contact(request):
    return render(request,'contact.html')


def emergency(request):
     return render(request,'emergency.html')


def finddoner(request):
     return render(request,'finddoner.html')


def Donors(request):
    a=Rdata.objects.all()
    return render(request,'donors.html',{'don':a})

def search(request):
     if request.method=='POST':
         DoG=request.POST.get('bldgrp')
         Dis=request.POST.get('dist')
         if Rdata.objects.filter(bgroup=DoG,district=Dis).exists():
             a = Rdata.objects.filter(bgroup=DoG,district=Dis)
             return render(request,'spcfdonors.html',{'don':a})
         else:
            messages.success(request, 'No Active Donors right now!')
            return redirect(finddoner)
     else:
        return redirect(finddoner)
     

def registration(request):
     if request.method=='POST':
        post=Rdata()
        post.name=request.POST['fullname']
        post.mobile=request.POST['mobile']
        post.email=request.POST['email']
        post.bgroup=request.POST['registerbloodgroup']
        post.bdate=request.POST['registerbirthdate']
        post.gender=request.POST['gender']
        post.weight=request.POST['registerweight']
        post.state=request.POST['registerstate']
        post.district=request.POST['registerdistrict']
        post.pincode=request.POST['pincode']
        post.save()
        messages.success(request, 'Registered Successfully!')
        return redirect(home)

     return render(request,'registration.html')

def logine(request):
     if request.method=='POST':
        username=request.POST.get('email')
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        user=authenticate(request,username=username,email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'login Successfully!')
            return redirect(home)
        else:
          #   messages.info(request,'user not exist')
            messages.success(request, 'user not exist')
            print('user not exist')
            return redirect(logine)     
     return render(request,'login.html')


def logoute(request):
    logout(request)
    return redirect(logine)
def signup(request):
     if request.method=='POST':
        username=request.POST.get('email')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('pass2')
        if password1==password2:
          if Udata.objects.filter(email=email):
            messages.success(request, 'useername already exists!')
            return redirect(signup)
          else:
               new_user1=Udata.objects.create(email=email,password=password1,password2=password2)
               new_user=User.objects.create_user(username=username,email=email,password=password1)
               new_user1.save()
               new_user.save()
               messages.success(request, 'SignUp Successfully!')
               return redirect(logine)
           
        else:
            messages.success(request, 'wrong Password!')
     return render(request,'signup.html')


def whydonate(request):
     return render(request,'whydonate.html')