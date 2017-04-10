from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^Lokahi', include('Lokahi_Fintech.urls')),
    url(r'^admin/', admin.site.urls),
]