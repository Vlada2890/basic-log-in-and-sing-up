# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def home(request):
    signup_form = UserCreationForm()
    login_form = AuthenticationForm()

    if request.method == 'POST':
        if 'signup' in request.POST:
            signup_form = UserCreationForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                auth_login(request, user)
                return redirect('home')
        elif 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user)
                return redirect('dairy')  # Przekierowanie na stronę dairy.html

    return render(request, 'users/home.html', {'signup_form': signup_form, 'login_form': login_form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dairy')  # Przekierowanie na stronę dairy.html
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})


@login_required
def dairy_view(request):
    return render(request, 'users/dairy.html')
