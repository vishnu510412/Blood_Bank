from django.contrib.messages.api import success
from django.shortcuts import render, redirect
from django.http import request
from django.contrib import messages , sessions
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


from .models import UserReg


ls = []
# Create your views here.
@login_required(login_url = '/')
def index(request):
    logindata = UserReg.objects.all()
    return render(request, 'display.html', {'datas': logindata})

@login_required(login_url='/')
def userdata(request):
    if request.method == 'POST':
        name = request.POST['user1']
        details = request.POST['dets']
        bl_group = request.POST['bgroup']
        age = request.POST['age']
        UserReg.objects.create(user1=name,donardts=details,bdgroup=bl_group,age=age)
        return redirect(index)
    return render(request,"home.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect(userdata)
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('userdata')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('userdata')

            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            print('Password not matching... ')
        return redirect(index)  # go back to home page
    return render(request, 'signup.html')
    


def user_login(request):

    if request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse(
                {'success':True},
                safe=False
            )
        else:
            return JsonResponse(
                {'success': False},
                safe=False
            )
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect(user_login)

