from . import views
from django.urls import path
urlpatterns =[path('abc', views.index ,name='index')]
