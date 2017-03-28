from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import HomepageInitialSettings, LinksBar, TechRiderArch, \
    TechRiderImg, CarouselImg
from news.views import *
from music.models import Album
from videos.models import Video
from shows.models import Poster

if len(HomepageInitialSettings.objects.all()) != 0:
    band = HomepageInitialSettings.objects.all()[0]
else:
    band = False
links = LinksBar.objects.all()



def homepage(request):
    if not band:
        return HttpResponse("Please go to administrative page and \
            fill in the Site's initial settings form. \
            Also for best site \
            performanse \
            add at least one video item, news item and album item with \
            soundcloud link")
    else:
        if len(Article.objects.all()) != 0:
            latestnews = Article.objects.filter(published_date__lte=\
                timezone.now()).order_by('-published_date')[0]
        else:
            latestnews = False

        if len(Album.objects.all()) != 0:
            soundcloud = Album.objects.all()[0].sc_link

        if len(Video.objects.all())!=0:
            video = Video.objects.all().order_by('-published_date')[0].vid

        carousels = CarouselImg.objects.all()
        carousels_length = len(carousels)
        if len(carousels) > 1:
            carousels_rest = CarouselImg.objects.all()[1:]
        else:
            carousels_rest = False

        if len(Poster.objects.all()) != 0:
            next_show = Poster.objects.filter(show_date__gte=timezone.now()).order_by\
                ('show_date')[0]
        else:
            next_show = False

        return render(request, 'home/homepage.html',
                {
                    'latestnews': latestnews,
                    'band': band,
                    'links': links,
                    'soundcloud': soundcloud,
                    'carousels': carousels,
                    'carousels_rest': carousels_rest,
                    'carousels_length': carousels_length,
                    'video': video,
                    'next_show': next_show
                }
            )


def riderpage(request):
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

    return render(request,
        'home/riderpage.html',
            {
                'techrider_arch': techrider_arch,
                'techrider_img': techrider_img,
                'band': band,
                'links': links
            }
        )
