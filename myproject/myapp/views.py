from django.shortcuts import render
import requests
from myapp.models import testtable
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
 return HttpResponse(request.POST)
 # testtb=testtable(Id="1", Name="Nimesh")
 # testtb.save()
 # objects=testtable.objects.all()
 # res="Entries in database:<br>"
 # for item in objects:
 #   res= res + ". " +item.Name +"<br>"
 # return HttpResponse(res)
# Create your views here.
