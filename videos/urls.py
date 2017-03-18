from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.videospage, name='videos'),
    url(r'^(?P<pk>\d+)/$', views.viewvideo, name='viewvideo'),
    url(r'^add/$', views.add_video, name='add_video'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit_video, name='edit_video'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete_video, name='delete_video'),
]
