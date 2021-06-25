

from django.contrib import admin
from django.urls import path
from .import views

app_name = 'typoapp'

urlpatterns = [
    path('', views.ko_sentiment, name = 'ko_sentiment'),
    path('show', views.show_mc, name = 'show_mc')
    ]
