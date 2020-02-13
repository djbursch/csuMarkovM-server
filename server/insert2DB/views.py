from django.shortcuts import render
from django.http import HttpResponse
from .models import Array
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

def index(request):
    latest_array_list = Array.objects.order_by('-pub_date')[:5]
    output = ', '.join([a.array_num for a in latest_array_list])
    return HttpResponse(output)

def singleArray(request, array_id):
	array = Array.objects.get(id=array_id)
	return HttpResponse(array)

def createArray(request):
	a = Array(array_num = "lets see if it works", pub_date=timezone.now())
	a.save()
	return HttpResponse(a)
