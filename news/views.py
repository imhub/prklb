from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import AddNewsForm



def newspage(request):
    news = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'home/newspage.html', {'news': news})

def readthenews(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'home/readthenews.html', {'article': article})

@login_required
def add_news(request):
    if request.method == "POST":
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            try:
                article.picture = request.FILES['picture']
            except KeyError:
                pass
            article.save()
            return redirect('readthenews', pk=article.pk)
    else:
        form = AddNewsForm()
    return render(request, 'home/news_edit.html', {'form': form})

@login_required
def edit_news(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = AddNewsForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            try:
                article.picture = request.FILES['picture']
            except KeyError:
                pass
            article.save()
            return redirect('readthenews', pk=article.pk)
    else:
        form = AddNewsForm(instance=article)
    return render(request, 'home/news_edit.html', {'form': form})
