from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^product/(?P<id>\d+)$', views.product),
    url(r'^wishlist/(?P<id>\d+)$', views.wishlist),
    url(r'^destroy/(?P<id>\d+)$', views.destroy)

]
