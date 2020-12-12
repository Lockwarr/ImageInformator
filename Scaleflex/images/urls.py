"""The 'urlpatterns' list routesURLs to views"""
from django.urls import path
from images import views

urlpatterns = [
    path('process', views.Images.as_view()),
]
