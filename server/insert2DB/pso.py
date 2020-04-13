from .models import Data
import numpy as np
import random as rm
import pyswarms as ps

def particleSwarmOptimization(request):
	
	data = request.POST.get('data')
	UnivGrad = data
	globalMinimum = 0
	##need to update with actual data
	parameters = [0,0,1,33,195,305]
	'''
	%Fall 2010 %
	UnivGrad10=[0,0,1,33,195,305];%univ grad
	UnivPers10=[439,416,410,353,184,59]; %Univ persist
	UnivRet10=[439,416,402,386,379,364]; %Univ retention
	
	'''

	localMinimum = 0
	'''
	NEED TO SEND TO TRAINING MODEL
	for t in range(0,100):

		lmbda -> random starting value within (0, .10)
		starting at t=1, initial value
		v(0) = 0 (nothing has moved yet)
		sigma -> random starting value wintin (0, .10)
		alpha -> random starting value wintin (0, .10)
		beta -> random starting value wintin (0, .10)
	'''
	##do the calculations (make a trainingModel.py)
	##get cohort grad (graduated)


	currentCost = cost(UnivGrad, graduated)
	if currentCost < localMinimum:
		localMinimum = currentCost
	if localMinimum < globalMinimum:
		globalMinimum = localMinimum


