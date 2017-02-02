from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^easyrider/$', views.riderpage, name='rider'),
]
