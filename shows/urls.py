from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.showspage, name='shows'),
    url(r'^(?P<pk>\d+)/$', views.shownfo, name='shownfo'),
    url(r'^add/$', views.add_show, name='add_show'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit_show, name='edit_show'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete_show, name='delete_show'),
]
