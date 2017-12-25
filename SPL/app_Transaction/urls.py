from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.checkPolyCardData),
    #path('', views.index, name='index'),
    #path('', views.registration, name='registration'),
]
