from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addentry$', views.addentry),
    url(r'^remove/(?P<id>\d+)$', views.remove)
]
