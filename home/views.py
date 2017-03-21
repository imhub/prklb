from django.shortcuts import render, redirect

from .models import HomepageInitialSettings, LinksBar, TechRiderArch, \
    TechRiderImg, CarouselImg
from news.views import *
from music.models import Album

if len(HomepageInitialSettings.objects.all()) != 0:
    band = HomepageInitialSettings.objects.all()[0]
links = LinksBar.objects.all()
if len(TechRiderArch.objects.all()) != 0:
    techrider_arch = TechRiderArch.objects.all()[0].archrider
else:
    techrider_arch = False
if 0 < len(TechRiderImg.objects.all()) <= 3:
    techrider_img = TechRiderImg.objects.all()
elif len(TechRiderImg.objects.all()) == 0:
    techrider_img = False
else:
    techrider_img = TechRiderImg.objects.all()[:3]
carousels = CarouselImg.objects.all()
if len(carousels) > 1:
    #carousel_0 = CarouselImg.objects.all()[0]
    carousels_rest = CarouselImg.objects.all()[1:]
carousels_length = len(carousels)

def homepage(request):
    if len(Article.objects.all()) != 0 and len(Album.objects.all()) != 0:
        latestnews = Article.objects.filter(published_date__lte=\
            timezone.now()).order_by('-published_date')[0]
        soundcloud = Album.objects.all()[0].sc_link
        return render(request, 'home/homepage.html',
                {
                    'latestnews': latestnews,
                    'band': band,
                    'links': links,
                    'soundcloud': soundcloud,
                    'carousels': carousels,
                    'carousels_rest': carousels_rest,
                    'carousels_length': carousels_length
                }
            )
    return redirect('/admin')

def riderpage(request):
    return render(request,
        'home/riderpage.html',
            {
                'techrider_arch': techrider_arch,
                'techrider_img': techrider_img,
                'band': band,
                'links': links
            }
        )
