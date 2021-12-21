from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import user_reg, book_details
from django.core.paginator import Paginator, EmptyPage


def login_render(request):
    ''' To render login page '''
    return render(request, 'login.html')


def home(request):
    ''' Add pagination '''
    books = book_details.objects.all().order_by('title')
    p = Paginator(books, 3)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request, 'home.html', {'books': page})


def register(request):
    ''' Get details from register page and save in user_details '''
    if request.method=='POST':
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
            return render(request, 'login.html');
        else:
            return HttpResponse("Password does not match with retype password")
    return render(request, 'register.html')


def login(request):
    ''' To check if already exists and login to the website '''
    username = request.POST['username']
    password = request.POST['password']
    user_list = user_reg.objects.all()
    for user in user_list:
        print(user.user_name)
        if user.user_name == username:
            if user.password == password:
                return redirect('home')
    return HttpResponse("Incorrect username or password!!")


def search(request):
    ''' Search for book with bookname '''
    book_name = request.GET.get('book_name')
    status = book_details.objects.filter(title__startswith=book_name)
    if status:
        return render(request, 'search.html', {'books': status})
    else:
        return HttpResponse("No such book found!!")


def search_category(request):
    ''' Search for books based on bookname '''
    category = request.GET.get('category')
    status = book_details.objects.filter(category__startswith=category)
    if status:
        return render(request, 'search.html', {'books': status})
    else:
        return HttpResponse("No such book found!!")


def checkout(request):
    ''' load checkout page '''
    return render(request, 'checkout.html')


def status(request):
    ''' Display status '''
    return HttpResponse("Book is on your way!! Happy Reading!!")
