from django.shortcuts import render
from .models import Article

def newspage(request):
    return render(request, 'home/newspage.html', {})

def newslist(request):
    news = Article.objects.all()
    return render(request, 'home/newspage.html', {'news': news})
