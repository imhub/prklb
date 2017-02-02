from django.shortcuts import render
from .models import HomepageInitialSettings
from news.views import *

def homepage(request):
    latestnews = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0]
    band = HomepageInitialSettings.objects.all()[0]
    return render(request, 'home/homepage.html', {'latestnews': latestnews, 'band': band})

def riderpage(request):
    techrider = HomepageInitialSettings.objects.all()[0].rider
    return render(request, 'home/riderpage.html', {'techrider': techrider})
