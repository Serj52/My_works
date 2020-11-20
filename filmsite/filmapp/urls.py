from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'simple_route\w{0,}', views.simple_route, name='simple_route'),
    path('sum_route/<number1>/<number2>/', views.sum_route, name='sum_route'),
    # re_path(r'sum_get_method/a=(\D{0,}\w)&b=(\D{0,}\w)', views.sum_get_method, name = 'sum_get_method'),
    re_path(r'sum_get_method/(?P<a>)/', views.sum_get_method, name = 'sum_get_method'),


]
