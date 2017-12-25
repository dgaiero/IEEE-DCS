from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^checkIn/$', views.checkIn),
    url(r'^checkInOrCheckOut/$', views.checkIn_Or_CheckOut),
    url(r'^checkOut/$', views.checkOut),
    url(r'^checkPolyCard/$', views.checkPolyCardData),
    url(r'^registration/$', views.registration),
    url(r'^transactionSummary/$', views.transaction_Summary),
]
