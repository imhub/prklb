from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT, DEBUG

urlpatterns = [
    url('', include('home.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^shows/', include('shows.urls')),
    url(r'^videos/', include('videos.urls')),
    url(r'^admin/', admin.site.urls),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
