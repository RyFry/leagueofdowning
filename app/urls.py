from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    
    url(r'^champions/$', views.champions),
    url(r'^champions/(?P<id>.*)', views.champion),
    url(r'^champions/*', views.champions),
    
    url(r'^items/$', views.items),
    url(r'^items/(?P<id>.*)', views.item),
    url(r'^items/*', views.items),

    url(r'^players/$', views.players),
    url(r'^players/(?P<id>.*)', views.player),
    url(r'^players/*', views.players),

    url(r'^.*/$', views.index)
]
