from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.newspage, name='news'),
    url(r'^(?P<pk>\d+)/$', views.readthenews, name='readthenews'),

]
