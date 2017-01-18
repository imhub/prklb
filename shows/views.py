from django.shortcuts import render
from django.http import HttpResponse


def showspage(request):
    return HttpResponse('<h1>ShowsList</h1>')
