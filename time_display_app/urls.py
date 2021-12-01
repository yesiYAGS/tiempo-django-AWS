from django.urls import path,include
from time_display_app import views

urlpatterns = [
    path('', views.index),
]