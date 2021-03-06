try:
    from django.conf.urls import patterns, handler404, handler500, include, url
except ImportError:
    from django.conf.urls.defaults import patterns, handler404, handler500, include, url
from django.contrib import admin
import django
if django.VERSION < (1, 7):
    admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
