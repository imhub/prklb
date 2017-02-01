from django.conf.urls import url
from . import views
 

urlpatterns = [
    url(r'^$', views.newspage, name='news'),
    url(r'^(?P<pk>\d+)/$', views.readthenews, name='readthenews'),
    url(r'^add/$', views.add_news, name='add_news'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit_news, name='edit_news'),
]
