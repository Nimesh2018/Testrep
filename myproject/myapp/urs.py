from . import views
from django.urls import path
urlpatterns =[path('insert', views.insert ,name='insert'),
             path('fetch', views.fetch ,name='fetch')]
