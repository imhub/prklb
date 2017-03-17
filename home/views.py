from django.shortcuts import render, redirect

from .models import HomepageInitialSettings, LinksBar
from news.views import *
from music.models import Album

if len(HomepageInitialSettings.objects.all()) != 0:
    band = HomepageInitialSettings.objects.all()[0]
links = LinksBar.objects.all()

def homepage(request):
    if len(Article.objects.all()) != 0 and len(Album.objects.all()) != 0:
        latestnews = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0]
        soundcloud = Album.objects.all()[0].sc_link
        return render(request, 'home/homepage.html', {
            'latestnews': latestnews, 'band': band, 'links': links, 'soundcloud': soundcloud})
    return redirect('/admin')

def riderpage(request):
    techrider = HomepageInitialSettings.objects.all()[0].rider
    return render(request, 'home/riderpage.html', {
        'techrider': techrider, 'band': band, 'links': links})
