from django.urls import path
from . import views

app_name = 'webucks'
urlpatterns = [
    path('', views.index, name = 'index'),
]
