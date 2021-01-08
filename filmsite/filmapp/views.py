from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import Film, Producer
from django.views.decorators.http import require_http_methods
import re
from django.shortcuts import redirect
from django.template import Template, Context

def redirect_view(request):
   return HttpResponseRedirect('http://127.0.0.1:8080/filmapp/film/')

def film(request, num):
    name = Film.objects.get(id = num)

    if num == '1':
        return render(request, 'filmapp/Django.html', {'name': name})
    elif num == '2':
        return render(request, 'filmapp/Mulholland_Drive.html', {'name': name})

