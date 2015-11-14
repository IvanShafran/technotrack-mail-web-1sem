from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^login/$', "django.contrib.auth.views.login", {"template_name": "login.html"}),
	url(r'^logout/$', "django.contrib.auth.views.logout", {"template_name": "logout.html"}),
]
