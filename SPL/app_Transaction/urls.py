from django.urls import path
from django.conf.urls import url

from . import views

#Remove index.html and replace with checkPolyCard

#make urls more dynamic check YouTube
urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^anotherAction/$', views.another_Action, name='another_Action'),
    url(r'^checkIn/$', views.checkIn, name='checkIn'),
    url(r'^checkInOrCheckOut/$', views.checkIn_Or_CheckOut, name='checkIn_Or_CheckOut'),
    url(r'^checkOut/$', views.checkOut, name='checkOut'),
    #url(r'^checkPolyCard/$', views.checkPolyCardData, name='checkPolyCardData'),
    url(r'^$', views.checkPolyCardData, name='checkPolyCardData'),
    url(r'^parts/$', views.parts, name='parts'),
    url(r'^registration/users$', views.registered_Users, name='registered_Users'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^transactionSummary/$', views.transaction_Summary, name='transaction_Summary'),
]
