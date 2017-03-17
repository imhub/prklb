from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.musicpage, name='music'),
    url(r'^(?P<pk>\d+)/$', views.viewalbum, name='viewalbum'),
    url(r'^add/$', views.add_album, name='add_album'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit_album, name='edit_album'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete_album, name='delete_album'),
]
