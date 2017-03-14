from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views
from django.conf.urls.i18n import i18n_patterns

from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT


urlpatterns = i18n_patterns(
    url('', include('home.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^shows/', include('shows.urls')),
    url(r'^videos/', include('videos.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
)

urlpatterns += [url(r'^i18n/', include('django.conf.urls.i18n'))]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
