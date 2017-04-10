from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
<<<<<<< HEAD
    url(r'^Lokahi', include('Lokahi_Fintech.urls')),
    url(r'^admin/', admin.site.urls),
]
=======
    # Examples:
    # url(r'^$', 'Crowdfunding.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^results/?$', 'cs3240-s17-team27.Crowdfunding.Lokahi_Fintech.views.search', name='results.html'),
]
>>>>>>> 49bc47b7f14e01af3ce0233a9fe431a934d568fd
