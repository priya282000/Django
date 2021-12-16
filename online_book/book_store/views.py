from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import render
from .models import user_reg, book_details


def home(request):

    return render(request, 'home.html')


def reg_render(request):
    return render(request, 'register.html')


def register(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    email = request.POST['email']
    user_list = user_reg.objects.all()
    for user in user_list:
        print(user.user_name)
        if user.user_name == username:
            return HttpResponse("Username already taken!! Enter new username!!")

    if password == repassword:
        reg = user_reg(first_name=fname, last_name=lname, user_name=username, password=password, email=email)
        reg.save()
    else:
        return HttpResponse("Password does not match with retype password")
    return render(request, 'login.html')


def login_render(request):
    return render(request, 'login.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user_list = user_reg.objects.all()
    for user in user_list:
        print(user.user_name)
        if user.user_name == username:
            if user.password == password:
                books = book_details.objects.all()
                return render(request, 'home.html', {'books': books})
    return HttpResponse("Incorrect username or password!!")
