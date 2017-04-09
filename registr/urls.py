from django.conf.urls import url
from . import views

urlpatterns = [url(r'^', views.RegisterFormView.as_view()),]