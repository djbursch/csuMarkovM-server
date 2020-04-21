from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import Permission
from django.contrib.auth import authenticate
from django.contrib.contenttypes.models import ContentType
from .models import Data, Invite, User, DeptConsumer, CollegeConsumer, UnivConsumer, SystemConsumer, DeptProvider, CollegeProvider, UnivProvider, SystemProvider, Developer
from .cohortModel import cohortTest, cohortTrain
from .pso import particleSwarmOptimization
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken, Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import json
from rest_framework_simplejwt.views import TokenObtainPairView 
import numpy as np
import io
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import Group


class HomePageView(APIView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class ChartsView(APIView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class LoginView(APIView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class RegisterView(APIView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

#getting users
class users(APIView):
  def get(self, request, **kwargs):
        users = User.objects.all()
        context = {'allusers': users}
        return render(request, 'index.html', context)

#Send email to user
@csrf_exempt
@api_view(["POST"])
def sendEmail(request):
  subject = 'Email from backend of csuMarkov'
  message = 'This email was sent from the back end.\n Hehe I am glad it works.'
  from_email = settings.EMAIL_HOST_USER
  to_list = ['lisa.star@csulb.edu', 'mehrdad.aliasgari@csulb.edu']
  send_mail(subject,message,from_email,to_list,fail_silently=False)
  success = "User emailed successfully"
  return HttpResponse(success)
  #send_mail('subject', 'body of the message', 'djbursch@sbcglobal.net', ['djbursch@gmail.com'])


#Creating a user
@csrf_exempt
@api_view(["POST"])
def createUser(request):
  user = User.objects.create_user(username = request.data.get('username'),
                                	email = request.data.get('email'),
                                	password = request.data.get('password'))
  success = "User created successfully"
  return HttpResponse(success)

def inviteUser(request):
	#ALLOWING ADMIN TO INVITE USERS TO SERVER
	success = "User created successfully"
	return HttpResponse(success)

#Give permissions
@csrf_exempt
@api_view(['POST'])
def givePerm(request):
  username = request.POST['username']
  password = request.POST['password']
	#NEED TO GET SPECIAL KEY FROM USER##############JSON TOKEN FROM SCHOOL MAYBE?
  user = authenticate(request, username = username, password = password)
  if user is not None:
    content_type = ContentType.objects.get_for_model(UnivProvider)
    all_permissions = Permission.objects.filter(content_type=content_type)
    user.user_permissions.set(all_permissions)
    user.has_perm('insert2DB.can_write_clg')
    return Response("success")
  else:
    success = "Permission was a failure :("
    return Response(success)

def getPerm(request):

  permissions = user.user_permission.get()
  return Response(permissions)

class index(APIView):
    permission_classes = (IsAuthenticated, "can_view_clg")

    def get(self, request):
        latestDataList = Data.objects.order_by('-pubDate')
        output = ', '.join([a.schoolName for a in latestDataList])
        return Response(output)

class singleData(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, schoolName, departmentName):
        try:
           data = Data.objects.get(schoolName = schoolName, departmentName = departmentName)
           output = str(data)
           return Response(output)
        except Data.DoesNotExist:
           data = "Oops! The data you're looking for does not exist."
           return Response(data)
        except Data.MultipleObjectsReturned:
           data = "Oops! That request returned too many responses."
           return Response(data)

class multipleData(APIView):
      permission_classes = (IsAuthenticated,)

      def get(self, request, schoolName):
        data = Data.objects.filter(schoolName = schoolName)
        if not data:
                output = "There is no school under that name"
        else:
                output = ', '.join([a.departmentName for a in data])
        return HttpResponse(output)

#Upload new data for a school in collection
def uploadFile(request):
	#turn file into json
	#pso = particleSwarmOptimization(request)
	markovModel = cohortTrain(pso)
	newData = Data(data = request.data.get('data'), 
		       schoolName = request.data.get('schoolName'), 
		       departmentName = request.data.get('departmentName'), 
		       markovModel = markovModel, 
		       pubDate = timezone.now())
	newData.save()
  #pso(newData)
  #save new greek letters to parameterModel HERE
	success = "Your data was saved successfully!"
	return Response(success)

#class for encoding arrays
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class testData(APIView): #gradRate
#Send a schools test data to the oracle
  def get(self, request, incomingStudents):
    data = cohortTest(incomingStudents)
    totalGraphs ={'NumOfFigures':len(data), 'Figures': data}
    json_dump = json.dumps(totalGraphs, cls=NumpyEncoder)
    return Response(json_dump)   

