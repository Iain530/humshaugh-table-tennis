from django.conf.urls import url
from humshaugh_table_tennis import views

app_name = 'humshaugh_table_tennis'

urlpatterns = [
    url('^$', views.home, name='home'),
    url('^club-nights/$', views.club_nights, name='club_nights'),
    url('^news/(?P<page>\d+)/$', views.news, name='news'),
    url('^contact-us/$', views.contact_us, name='contact_us'),
    url('^rules/$', views.rules, name='rules'),
    url('^rules-full/$', views.rules_full, name='rules_full'),
    url('^location/$', views.location, name='location'),
##    url('^login/$', views.login, name='login'),

]
