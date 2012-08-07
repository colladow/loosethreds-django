from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gifs.views.index', name='home'),
    # url(r'^loosethreds/', include('loosethreds.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^users/(?P<user_id>\d+)$', 'gifs.views.show_user'),
    url(r'^users/(?P<user_id>\d+)/images/$', 'gifs.views.create'),
    url(r'^users/(?P<user_id>\d+)/images/(?P<image_id>\d+)/$',
        'gifs.views.delete'),

    url(r'login/$', 'django.contrib.auth.views.login'),
    url(r'logout/$', 'django.contrib.auth.views.logout_then_login'),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
