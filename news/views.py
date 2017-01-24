from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Article

def newspage(request):
    news = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'home/newspage.html', {'news': news})

def readthenews(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'home/readthenews.html', {'article': article})
