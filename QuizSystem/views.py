from django.shortcuts import render,redirect
from .models import Users
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        try:
            getEmail = request.POST.get('email')
            getPassword = request.POST.get('password')
            getUsers = Users.objects.get(email=getEmail)
            print(getUsers)
            print("true")
            if (getUsers.email == getEmail and getUsers.password == getPassword):
                return redirect('register')
        except Users.DoesNotExist:
            getUsers = None
            if(getUsers == None):
                print("Email id or password is wrong")
                return render(request,"login.html")
    return render(request,"login.html")


def register(request):
    if request.method == 'POST':
        getName = request.POST.get('name')
        getEmail = request.POST.get('email')
        getUniversity = request.POST.get('university')
        getCity = request.POST.get('city')
        getPhone = request.POST.get('phone')
        getPass = request.POST.get('pass')
        getConfPass = request.POST.get('confpass')
        if(getPass == getConfPass):
            objuser = Users(name=getName, email=getEmail,university=getUniversity,city=getCity,phone=getPhone,password=getPass)
            objuser.save()
            return redirect('login')
        else:
            print("Passwords dont match.")
            return render(request,"register.html")
    return render(request,"register.html")
