from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    (r'^beta/$', 'djangit.views.beta'),
    (r'^beta/(?P<beta_id>\d+)/$', 'djangit.views.beta'),
    (r'^release/$', 'djangit.views.release'),
    (r'^release/(?P<release_id>\d+)/$', 'djangit.views.release'),
    (r'', 'djangit.views.index'),
)
