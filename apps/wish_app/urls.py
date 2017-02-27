from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^process$', views.process, name='process'),
    url(r'^display/(?P<item_id>\d+)$', views.display, name='display'),
    url(r'^join/(?P<item_id>\d+)$', views.join, name='join'),
    url(r'^delete/(?P<item_id>\d+)$', views.delete, name='delete'),
    url(r'^remove/(?P<item_id>\d+)$', views.remove, name='remove'),
    url(r'^logout/(?P<item_id>\d+)$', views.logout, name='logout'),
]
