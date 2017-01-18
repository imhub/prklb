from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('', include('home.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^shows/', include('shows.urls')),
    url(r'^videos/', include('videos.urls')),
    url(r'^admin/', admin.site.urls),
]
