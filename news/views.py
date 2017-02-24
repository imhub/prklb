from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Article
from .forms import AddNewsForm, EditNewsForm
from home.models import HomepageInitialSettings, LinksBar

band = HomepageInitialSettings.objects.all()[0]
links = LinksBar.objects.all()

def newspage(request):
    news = Article.objects.filter(published_date__lte=timezone.now()).order_by(
        '-published_date')
    paginator = Paginator(news, 5)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, 'home/newspage.html', {
        'news': news, 'band': band, 'links': links})

def readthenews(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'home/readthenews.html', {
        'article': article, 'band': band, 'links': links})

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
            messages.success(request, "You added news article successfully!")
            return redirect('readthenews', pk=article.pk)
    else:
        form = AddNewsForm()
    return render(request, 'home/news_add.html', {
        'form': form, 'band': band, 'links': links})

@login_required
def edit_news(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = EditNewsForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            article.published_date = timezone.now()
            try:
                article.picture = request.FILES['picture']
            except KeyError:
                pass
            article.save()
            messages.success(request, "Changes saved!")
            return redirect('readthenews', pk=article.pk)
    else:
        form = EditNewsForm(instance=article)
    return render(request, 'home/news_edit.html', {
        'form': form, 'band': band, 'links': links})

@login_required
def delete_news(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    messages.success(request, "News article deleted")
    return redirect('news')
