from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test/$', views.test_page, name='test'),
    url(r'^home/$', views.home_page, name='home'),
    url(r'^event/(?P<id>\d+)/$', views.event_lineup, name='event_detail'),
    url(r'^drink/(?P<id>\d+)/$', views.drink_info, name='drink_info'),
    url(r'^ratings_list/(?P<fk>\d+)/$', views.drink_comments, name='drink_comments_rest'),
    url(r'^ratings_list/$', views.ratings_list, name='ratings_list')
]
