from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^test', views.test, name='test'),
    url(r'^players', views.players, name='players'),
    url(r'^items', views.items, name='items'),

    url(r'^champions', views.champions, name='champions'),
    url(r'^champions/dr_mundo', views.mundo, name='dr_mundo'),
    url(r'^champions/azir', views.azir, name='azir'),
    url(r'^champions/ezreal', views.ezreal, name='ezreal'),
]
