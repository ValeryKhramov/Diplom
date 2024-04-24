from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import LoginUserForm


def index(request):
    return render(request, 'base.html', {'title': 'Главная страница'})


def services(request):
    return render(request, 'myapp/services.html', {'title': 'Услуги'})


def contacts(request):
    return render(request, 'myapp/contacts.html', {'title': 'Контакты'})


def account(request):
    return render(request, 'myapp/personal_account.html', {'title': 'Личный кабинет'})


def history(request):
    return render(request, 'myapp/history.html', {'title': '"График работы"'})


def montage(request):
    return render(request, 'myapp/montage.html', {'title': '"История монтажа"'})


def inputs(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse(account))
    else:
        form = LoginUserForm()
    return render(request, 'myapp/input.html', {'title': 'Вход', 'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))
