from django.http import HttpResponse
from .models import Array
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .oracle import Oracle

def index(request):
	latest_array_list = Array.objects.order_by('-pub_date')[:20]
	output = ', '.join([a.array_num for a in latest_array_list])
	return HttpResponse(output)

def singleArray(request, array_id):
	array = Array.objects.get(id=array_id)
	return HttpResponse(array)

def createArray(request):
	newArray = Array(array_num=request.POST.get('array_num'), pub_date=timezone.now())
	newArray.save()
	return HttpResponse(newArray)

def stdDev(request, array_id):
	array = Oracle(array_id)
	return HttpResponse(array)
