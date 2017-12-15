"""SPL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

####################################################
#This is the master urls.py file for the SPL Project
####################################################

from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('app_Another_Action/', include('app_Another_Action.urls')),
    path('app_checkIn/', include('app_CheckIn.urls')),
    path('app_CheckIn_Or_CheckOut/', include('app_CheckIn_Or_CheckOut.urls')),
    path('app_CheckOut/', include('app_CheckOut.urls')),
    path('app_CheckOut_Express/', include('app_CheckOut_Express.urls')),
    path('app_CheckOut_Reg/', include('app_CheckOut_Reg.urls')),
    path('app_Registration/', include('app_Registration.urls')),
    path('app_Swipe_PolyCard/', include('app_Swipe_PolyCard.urls')),
    path('app_Transaction_Summary/', include('app_Transaction_Summary.urls')),
    path('admin/', admin.site.urls),
]
