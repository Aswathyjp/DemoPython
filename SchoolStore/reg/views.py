from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .form import mform
from . models import dispform


# Create your views here.
# def register(request):
#     if request.method=='POST':
#         username=request.POST["username"]
#         password=request.POST["password"]
#         confirm_pwd=request.POST["password1"]
#         if password==confirm_pwd:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"username taken")
#                 return redirect("register")
#             elif User.objects.filter(password=password).exists():
#                 messages.info(request, "password not matching")
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, password=password,confirm_password=confirm_pwd)
#                 user.save()
#                 return redirect('login')
#         else:
#             messages.info(request, "password not matching")
#             return redirect('register')
#         # return redirect('/')
#
#     return render(request,'Register.html')


# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return  redirect('/')
#         else:
#             messages.info(request,'Invalid user, click the link to register')
#             return redirect('login')
#     return  render(request,'Login.html')

def regform(request):
    return render(request,'registrationform.html')

def newform(request):
    return render(request,'newpage.html')

def register(request):

    if request.method == 'POST':
        username = request.POST['username']

        # email = request.POST['email']
        password = request.POST['password']
        confirm_pwd = request.POST['password1']
        if password == confirm_pwd:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect("register")
            elif User.objects.filter(password=password).exists():
                messages.info(request,"password taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save();
                # print("user created")
                return redirect('reg:login')

        else:
            # print("password not matching")
             messages.info(request,"password not matching")
             return redirect('register')
        return redirect('/')
    return render(request, 'Register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('reg:newform')
        else:
            messages.info(request,"Invalid")
            return redirect('reg:login')
    return render(request,'Login.html')
def logout(request):
     auth.logout(request)
     return redirect('/')

