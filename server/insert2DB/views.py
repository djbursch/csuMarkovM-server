from django.http import HttpResponse
from django.utils import timezone
from .models import Data
from .oracle import oracle, oracleTrain

#For getting all items in data collection
def index(request):
	latestDataList = Data.objects.order_by('-pubDate')
	output = ', '.join([a.schoolName for a in latestDataList])
	return HttpResponse(output)

#Getting a single departments data in collection
def singleData(request, schoolName, departmentName):
	try:
	   data = Data.objects.get(schoolName=schoolName, departmentName=departmentName)
	except Data.DoesNotExist:
	   data = "Oops! The data you're looking for does not exist."
	except Data.MultipleObjectsReturned:
	   data = "Oops! That request returned too many responses."  
	return HttpResponse(data)

#Getting all the departments from one school
def multipleData(request, schoolName):
	data = Data.objects.filter(schoolName = schoolName)
	if not data:
		output = "There is no school under that name"
	else:
	   	output = ', '.join([a.departmentName for a in data])
	return HttpResponse(output)

#Upload new data for a school in collection
def uploadData(request):
	markovModel = oracleTrain(request)
	newData = Data(data = request.POST.get('data'), 
		       schoolName = request.POST.get('schoolName'), 
		       departmentName = request.POST.get('departmentName'), 
		       markovModel = markovModel, 
		       pubDate = timezone.now())
	newData.save()
	return HttpResponse(newData)

#Send a schools data to the oracle
def testOracle(request):
	output = oracle(request)
	return HttpResponse(output)
