from django.shortcuts import render
from news.views import *



def videospage(request):
    latestnews = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0]
    return render(request, 'home/homepage.html', {'latestnews': latestnews})
