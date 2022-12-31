from .import views
from django.urls import path

urlpatterns = [
    path('home', views.base,name='base'),
    path('index', views.index,name='index'),
]