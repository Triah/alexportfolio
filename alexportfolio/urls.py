from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('gallery.urls')),
    url(r'^contact', include('contact.urls')),
    url(r'^about', include('about.urls')),
    url(r'^showreel', include('showreel.urls'))
]
