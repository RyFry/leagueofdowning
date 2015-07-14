from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^test', views.test, name='test'),
    
    url(r'^champions/$', views.champions, name='champions'),
    url(r'^champions/dr_mundo', views.mundo, name='dr_mundo'),
    url(r'^champions/azir', views.azir, name='azir'),
    url(r'^champions/ezreal', views.ezreal, name='ezreal'),
    url(r'^champions/*', views.champions, name='champions'),
    
    url(r'^items/$', views.items, name='items'),
    url(r'^items/athenes_unholy_grail', views.athenes, name='athenes'),
    url(r'^items/rabadons_deathcap', views.rabadons, name='rabadons'),
    url(r'^items/sorcerers_shoes', views.sorc_shoes, name='sorc_shoes'),
    url(r'^items/*', views.items, name='items'),

    url(r'^players/$', views.players, name='players'),
    url(r'^players/balls', views.balls, name='balls'),
    url(r'^players/bjergsen', views.bjergsen, name='bjergsen'),
    url(r'^players/doublelift', views.doublelift, name='doublelift'),
    url(r'^players/*', views.players, name='players'),

    url(r'^.*/$', views.index, name='index')
] 
