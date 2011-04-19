from django.conf.urls.defaults import *
from community import views

urlpatterns = patterns('',
    url(r'^$', views.community, name='community'),
)

