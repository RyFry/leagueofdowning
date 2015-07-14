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

    url(r'^api/champions/$', views.Champion_List_API),
    url(r'^api/champions/(?P<id>.*)/$',  views.Champion_ID_API),   
    url(r'^api/players/$',  views.Player_List_API),
    url(r'^api/players/(?P<id>.*)/$',  views.Player_ID_API),   
    url(r'^api/items/$',  views.Item_List_API),
    url(r'^api/items/(?P<id>.*)/$',  views.Item_ID_API),   

    url(r'^.*/$', views.index)
]
