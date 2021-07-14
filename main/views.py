from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import User
from .models import Task
from .forms import TaskForm, RegistrationForm, LoginForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about_us(request):
    return render(request, 'main/about_us.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верна'
    form = TaskForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/create.html', context)


def registration(request):
    error = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верна'
    form = RegistrationForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/registration.html', context)


#def register_new_user(username, password):
    #return User.objects.create_user(username=username, password=password)


def login(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верна'
    form = LoginForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/login.html', context)
