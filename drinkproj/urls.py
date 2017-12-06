from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test/$', views.test_page, name='test'),
    url(r'^home/$', views.home_page, name='home'),
    url(r'^home/(?P<id>\d+)/$', views.event_lineup, name='event_detail'),

]
