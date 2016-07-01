from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^main/(?P<pk>\d+)/$', views.mainarticle, name='mainarticle'),

]