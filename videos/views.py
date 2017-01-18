from django.shortcuts import render
from django.http import HttpResponse


def videospage(request):
    return HttpResponse('<h1>VideosList</h1>')
