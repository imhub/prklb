from django.shortcuts import render
from django.http import HttpResponse


def newspage(request):
    return HttpResponse('<h1>NewsList</h1>')
