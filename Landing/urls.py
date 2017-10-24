from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex /landing/base
    url(r'^base/$', views.base, name='base'),
    # ex /landing/about
    url(r'^about/$', views.about, name='about'),
    url(r'^submission/$', views.submission, name='submission'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^memberbase/$', views.sidebase, name='member'),
    url(r'^test/$', views.test, name='test'),
]