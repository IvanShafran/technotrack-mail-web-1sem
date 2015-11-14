from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.show_question, name='show_question'),
    url(r'new/$', views.new_question, name='new_question'),
]