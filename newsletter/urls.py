from django.conf.urls import url

from newsletter import views

urlpatterns = [
    url(r'^$', views.index, name='newsletter'),
]