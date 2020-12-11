from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    re_path(r'^film/(?P<film_id>tt\d{7,8})/$', views.film, name='film'),
    re_path(r'^film/(?P<film_id>tt\d{7,8})/new/$', views.review_new, name='review_new'),
]
