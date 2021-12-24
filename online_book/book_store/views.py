from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import user_reg, book_details
from django.core.paginator import Paginator, EmptyPage
from .forms import RegistrationForm, LoginForm


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
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html', {'form': form})


def login(request):
    ''' To check if already exists and login to the website '''
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            return redirect('home')
    return render(request, 'login.html', {'form': form})


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
