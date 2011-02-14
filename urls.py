from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'www.views.index'),
    (r'^styles/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^login',  'www.views.login'),
    (r'^logout', 'www.views.logout'),
#    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^(?P<user_name>[a-zA-Z0-9\-]+)/$', 'www.views.user'),
    (r'^api/programs', 'www.views.post_programs'),
    # Example:
    # (r'^myprogs/', include('myprogs.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:

    # Uncomment the next line to enable the admin:

)

