from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))
