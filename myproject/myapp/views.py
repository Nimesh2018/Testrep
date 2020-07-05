from django.shortcuts import render
import requests
from myapp.models import posttable
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def insert(request):
 # return HttpResponse(request)
   tableobj=posttable(Emp_name=request.POST.get("Emp_name",""))
   tableobj.save()
 # res="Entries in database:<br>"
 # return HttpResponse(res)


@csrf_exempt
def fetch(request):
  objects=posttable.objects.all()
  data=[]
  for item in objects:
    row={'Id': item.Emp_id, 'Name': item.Emp_name}
    data.append(row)
  return JsonResponse(data,safe=False)   
