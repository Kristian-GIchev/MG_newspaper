from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from MG_vestnik.settings import LOGIN_URL
from MG_vestnik.mg_auth.forms import LoginForm


def u_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
        'name': 'Register Page'
    }
    return render(request, 'register.html', context)


def u_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form': form,
        'name': 'Login Page',
    }
    return render(request, 'login.html', context)


@login_required(login_url=LOGIN_URL)
def u_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    else:
        return render(request, 'logout.html', context={'name': 'Log Out Page'})
