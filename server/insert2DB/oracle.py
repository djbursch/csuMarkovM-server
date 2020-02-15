from .models import Data
import numpy as np
import random as rm

#This is where the matlab code is going to be translated
#Just created the pipeline so it's ready to receive data

def oracle(request):
	#This is for when the model is already trained
	data = request.POST.get('data')
	markovModel = 1
	return markovModel

def oracleTrain(request):
	#Do the training calculations in here
	data = request.POST.get('data')
	markovModel = 1
	return markovModel
