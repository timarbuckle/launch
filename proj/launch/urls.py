from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from .views import HomeView, AuthView, LoginView, LogoutView

urlpatterns = patterns('',
    url(r'^launch$', HomeView.as_view(), name='home'),
    url(r'^launch/auth$', AuthView.as_view(), name='auth'),
    url(r'^launch/login$', LoginView.as_view(), name='login'),
    url(r'^launch/logout$', LogoutView.as_view(), name='logout'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^launch/admin/', include(admin.site.urls)),
)
