from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('app_Swipe_PolyCard/', include('app_Swipe_PolyCard.urls')),
    path('admin/', admin.site.urls),
]
