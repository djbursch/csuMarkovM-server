from django.http import HttpResponse
from .models import Data
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .oracle import Oracle

def index(request):
	latest_data_list = Data.objects.order_by('-pubDate')
	output = ', '.join([a.schoolData for a in latest_data_list])
	return HttpResponse(output)

def singleData(request, schoolName):
	data = Data.objects.get(schoolName=schoolName)
	return HttpResponse(data)

def createData(request):
	newData = Data(schoolData=request.POST.get('schoolData'), schoolName=request.POST.get('schoolName'), departmentName=request.POST.get('departmentName'), pubDate=timezone.now())
	newData.save()
	return HttpResponse(newData)

def oracle(request, schoolName):
	output = Oracle(schoolName)
	return HttpResponse(output)
