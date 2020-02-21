from .models import Data
import numpy as np
import random as rm

#This is where the matlab code is going to be translated
#Just created the pipeline so it's ready to receive data

def markov(request):
	#This is for when the model is already trained
	data = request.POST.get('data')
	markovModel = 1
	return markovModel

def markovTrain(pso):
	#Do the training calculations in here
	data = request.POST.get('data')
	markovModel = 1
	
	##Inputs
	n = 8 #number of semesters in road map
	k = 15 #number of semesters to model
	p=0; #steady state trigger, if p=1 steady-state, p=0 only add students in year 1 
	h=0; #college trigger, if h=1, only calc College, if =0, calc university
	q=0; #system shock trigger, if q=1, add shock semester 15, if q=0 just steady state

	#Calibration Factors:
	ones=[0,1,1,1,1,1,1,1,1];
	COEUnits=[0,3.5,3.5,5,5,12,12,13,13];
	incoming=710*[0,1,0,0,0,0,0,0,0,0]; #[.47,0.01,.01,0.01,.47,0.01,.01,0.01];%number of student entering into each class at time k
	sigma=0.02*[0,3.6,1,1,1,1,1,1,1,1]; #University withdrawal rate (1-retained)for each class at time k
	beta=0.05*ones; #DFW rate for each class at time k (need to repeat)
	alpha=0.15*ones; #slowing factor to account for students taking less than 15 units per semester (need additional semester to complete class)
	lmbda=h*0.025*[0,4,2,2,1,.5,.5,.5,.5,.5]; #could include "migrating" to allow calculation of grad in and out of COE

	#Preallocate Matrices 
	time=np.linspace(0,k,k+1);
	time1=np.linspace(0,k-1,k);
	x=np.zeros(n+1,k+1);
	x_migration=np.zeros(n+1,k+1);
	x_DFW=np.zeros(n+1,k+1);
	x_slowed=np.zeros(n+1,k+1);
	x_Withdraw=np.zeros(n+1,k+1);
	x_advance=np.zeros(n+1,k+1);
	y=np.zeros(1,k+1);
	retained=np.zeros(1,k+1);
	graduated=np.zeros(1,k+1);
	number_of_units_attempted=np.zeros(1,k+1);
	number_of_units_DFWed=np.zeros(1,k+1);
	cohortretention=np.zeros(1,k+1);
	cohortpersistance=np.zeros(1,k+1);
	cohortgrad=np.zeros(1,k+1);


	return markovModel
