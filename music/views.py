from django.shortcuts import render
from django.http import HttpResponse


def musicpage(request):
    return HttpResponse('<h1>AlbumsList</h1>')
