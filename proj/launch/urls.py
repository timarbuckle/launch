from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^launch$', 'launch.views.home', name='home'),
    url(r'^launch/auth$', 'launch.views.auth', name='auth'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^launch/admin/', include(admin.site.urls)),
)
