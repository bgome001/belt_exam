from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^formView$', views.formView),
    url(r'^create$', views.create),
    url(r'^delete$', views.delete),
]
