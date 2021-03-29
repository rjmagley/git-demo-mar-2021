from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_thing', views.add_new_thing)
]