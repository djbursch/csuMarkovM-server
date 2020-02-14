from django.http import HttpResponse
from .models import Data, markovModel
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .oracle import Oracle

#For getting all items in data collection
def index(request):
	latest_data_list = Data.objects.order_by('-pubDate')
	output = ', '.join([a.schoolName for a in latest_data_list])
	return HttpResponse(output)

#Getting a single schools data in collection
def singleData(request, schoolName):
	data = Data.objects.get(schoolName=schoolName)
	return HttpResponse(data)

#Create new data for a school in collection
def createData(request):
	newData = Data(schoolData=request.POST.get('schoolData'), schoolName=request.POST.get('schoolName'), departmentName=request.POST.get('departmentName'), pubDate=timezone.now())
	newData.save()
	return HttpResponse(newData)

#Send a schools data to the oracle
def oracle(request, schoolName):
	output = Oracle(schoolName)
	return HttpResponse(output)
