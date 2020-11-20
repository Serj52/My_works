from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Film, Producer
import re
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
def simple_route(request):
    if request.method == 'GET':
        if str(request.path) == '/filmapp/simple_route/':
            return HttpResponse(content='ОК', status='200')
        elif str(request.path) == re.findall(r'/filmapp/simple_route/\w+.*', str(request.path))[0]:
            return HttpResponse(status='404')
    elif request.method == 'POST' or request.method == 'PUT':
        return HttpResponse(status='405')

def sum_route(request, number1, number2):
    try:
        res = int(number1) + int(number2)
        return HttpResponse(content=res, status='200')
    except ValueError:
        return HttpResponse(status='404')

@require_http_methods(['GET'])
def sum_get_method(request, a = 'a', b = 'b'):
    try:
        res = int(a) + int(b)
        return HttpResponse(content=res, status='200')
    except ValueError:
        return HttpResponse(status='400', content='Ошибка')