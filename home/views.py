from django.shortcuts import render

from .models import HomepageInitialSettings, LinksBar
from news.views import *

band = HomepageInitialSettings.objects.all()[0]
links = LinksBar.objects.all()

def homepage(request):
    latestnews = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0]
    return render(request, 'home/homepage.html', {
        'latestnews': latestnews, 'band': band, 'links': links, 'available_languages': ['en', 'uk', 'de']})

def riderpage(request):
    techrider = HomepageInitialSettings.objects.all()[0].rider
    return render(request, 'home/riderpage.html', {
        'techrider': techrider, 'band': band, 'links': links})
