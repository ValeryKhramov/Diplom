from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1 style='text-align:center;'>Добро пожаловать в Django</h1>")
