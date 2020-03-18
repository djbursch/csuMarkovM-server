from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from .models import Data, Invite, DeptConsumer, CollegeConsumer, UnivConsumer, SystemConsumer, DeptProvider, CollegeProvider, UnivProvider, SystemProvider, Developer
from .markov import markov, markovTrain
from .pso import particleSwarmOptimization
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken, Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import jwt,json
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView 
import numpy as np
import io


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class ChartsView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class LoginView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class RegisterView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

#getting users
class users(TemplateView):
  def get(self, request, **kwargs):
        users = User.objects.all()
        context = {'allusers': users}
        return render(request, 'index.html', context)

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
	user = authenticate(request, 
			    username = username, 
			    password = password)
	if user is not None:
		#This content_type is for testing, need to get JSON token for actual verification
		content_type = ContentType.objects.get_for_model(CollegeConsumer)
		all_permissions = Permission.objects.filter(content_type__app_label = 'insert2DB', 
							    content_type__model = content_type)
		user.user_permissions.set(all_permissions)
		return HttpResponse("success")
	else:
		success = "Permission was a failure :("
		return HttpResponse(success)

'''
#Log the user in for the session
@api_view(["POST"])
def userLogin(request):
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(request,username = username,password = password)
          if user is not None:
                payload = {
                  'id': user.id,
                  'email': user.email,
                }
                token = Token(user, 5)
                token['name'] = user.name

                return HttpResponse(
                json.dumps(token),
                status=200,
                content_type="application/json"
                )
          else:
            	return Response(
                json.dumps({'Error': "Invalid credentials"}),
                status=400,
                content_type="application/json")
'''

#Log the user out for the session
def userLogout(request):
    logout(request)
    output = "logout was a success!"
    return HttpResponse(output)

class index(APIView):
    permission_classes = (IsAuthenticated,)

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
	pso = particleSwarmOptimization(request)
	markovModel = markovTrain(pso)
	newData = Data(data = request.data.get('data'), 
		       schoolName = request.data.get('schoolName'), 
		       departmentName = request.data.get('departmentName'), 
		       markovModel = markovModel, 
		       pubDate = timezone.now())
	newData.save()
	success = "Your data was saved successfully!"
	return HttpResponse(success)

class testData(APIView):
#Send a schools test data to the oracle
  def get(self, request, incomingStudents):
    data = markovTrain(incomingStudents)
    print(data)
    success = "it works"
    return HttpResponse(data)

