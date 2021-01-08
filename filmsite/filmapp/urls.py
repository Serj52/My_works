from django.urls import path, re_path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('film/<num>/', views.film, name='film'),
    path('all/', RedirectView.as_view(url = 'http://127.0.0.1:8080/filmapp/film/')),



]

