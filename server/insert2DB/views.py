from django.http import HttpResponse
from django.utils import timezone
from .models import Data
from .oracle import oracle, oracleTrain
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

#Creating a user
def createUser(request):
	user = User.objects.create_user(username = request.POST.get('username'),
                                 email = request.POST.get('email'),
                                 password = request.POST.get('password'))
	success = "User created successfully"
	return HttpResponse(success)

#Log the user in for the session
def userLogin(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		output = "login was a success!"
	else:
		output = "login was a failure :("
	return HttpResponse(output)

#Log the user out for the session
def userLogout(request):
	logout(request)
	output = "logout was a success!"
	return HttpResponse(output)

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

