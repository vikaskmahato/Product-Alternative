from django.shortcuts import render, redirect
from .models import Profile
from .forms import Profileform, Searchform
from .forms import Registerform
from .forms import Loginform
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def profileupdate(request):
    prof=Profile.objects.get(user=request.user)
    form=Profileform(request.POST or None, request.FILES or None, instance=prof)  #files for photo,none for blank form


    if request.method=='POST':
        if form.is_valid():
            form.save()
            


    context={
        'Profile':prof,
        'form':form,
        
    }
    return render(request, 'accounts/profile.html', context)

def searching(request):
    if request.method=='POST':
        nm=request.POST['name']
        s=Profile.objects.filter(category=nm)
        sform=Searchform()
        return render(request, 'accounts/search.html',{'Profiles':s, 'sform':sform})
    else:
        sform=Searchform()
        return render(request, 'accounts/search.html', {'sform':sform})

   

def register(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                User.objects.get(username=request.POST['name'])
                return render(request,'accounts/register.html',{'error':'Username already exists'})
            except :
                user=User.objects.create_user(request.POST['name'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('business')
        else:
            f=Registerform()
            return render(request,'accounts/register.html',{'error':'Password does not match','form1':f})
    else:
        f=Registerform()
        return render(request,'accounts/register.html',{'form1':f})        


def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['name'],password=request.POST['password1'])
        if user is not None:
            auth.login(request,user)
            return redirect('business')
        else:
            f1=Loginform()
            return render(request,'accounts/login.html',{'error':'Username or password is incorrect','form2':f1})
    else:
        f1=Loginform()
        return render(request,'accounts/login.html',{'form2':f1}) 


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')        


def home (request):
    return render(request, 'accounts/home.html')

def business (request):
    return render(request, 'accounts/business.html')

def visit (request, id):
    p=Profile.objects.filter(pk=id)
    return render(request, 'accounts/visitprofile.html', {'VProf':p})

def viewprofile(request):
    prof=Profile.objects.get(user=request.user)
    return render(request, 'accounts/viewprofile.html', {'Profile':prof})

