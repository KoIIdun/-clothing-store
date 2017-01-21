from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^(?P<product_id>[0-9]+)/$', views.product_info, name="product_info"),
    url(r'^', views.index),
]
