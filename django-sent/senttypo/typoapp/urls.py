
from django.contrib import admin
from django.urls import path
from typoapp import views


urlpatterns = [
    path('', views.ko_sentiment, name = 'ko_sentiment')
    ]
