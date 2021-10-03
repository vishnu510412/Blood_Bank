from django.shortcuts import render, redirect
from django.http import request
from django.contrib import messages
from django.contrib.auth.models import User, auth

from .models import UserReg


ls = []
# Create your views here.

def index(request):

    logindata = UserReg.objects.all()

    return render(request, 'display.html', {'datas': logindata})


def userdata(request):
    if request.method == 'POST':
        name = request.POST['user1']
        details = request.POST['dets']
        bl_group = request.POST['bgroup']
        age = request.POST['age']
        # res = {
        #     "username": name,
        #     "userdetails": details,
        #     "bloodgroup": bl_group,
        #     "userage": age
        # }
        logindata = UserReg.objects.create(user1=name,donardts=details,bdgroup=bl_group,age=age)
        # logindata.save(); WS

        rg = UserReg.objects.all()


        print('Added successfully')    

        return render(request,"display.html",{'datas':rg})
        

        return render(request,'display.html')

        return render(request, 'display.html', {'datas': logindata})
      

        # ls.append(res)
        return redirect(index)
    return render(request, 'home.html')


def signup(request):

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
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            print('Password not matching... ')
        return redirect('/')  # go back to home page

    else:

        return render(request, 'signup.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials Try Again')
            return redirect('login')
    else:
        return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

