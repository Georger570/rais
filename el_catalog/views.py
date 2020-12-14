from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
    return render(request, "login.html", {})

def index(request):
    #user = User.objects.create_user('john@mail.ru', 'lennon@thebeatles.com', 'johnpassword')
    if request.user.is_authenticated:
        return render(request, "base.html", {})
    else:
        return redirect('/login/')