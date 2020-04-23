from .models import Data
import numpy as np
import random as rm
from django.http import HttpResponse


def cohortTrain(nStudents, sigma, beta, alpha, lmbda):
	#This is for when the model is already trained
	N10=488
	##Inputs
	n = 8 #number of semesters in road map
	k = 15 #number of semesters to model
	p = 0 #steady state trigger, if p=1 steady-state, p=0 only add students in year 1 
	h = 0 #college trigger, if h=1, only calc College, if =0, calc university
	q =0 #system shock trigger, if q=1, add shock semester 15, if q=0 just steady state

	#Calibration Factors:
	#incomingStudents = request.data.get('students')
	##Calibration factors for PSO
	ones=[0,1,1,1,1,1,1,1,1]
	COEUnits=[0,3.5,3.5,5,5,12,12,13,13]
	incoming=N10*np.asarray([0,1,0,0,0,0,0,0,0,0]) #[.47,0.01,.01,0.01,.47,0.01,.01,0.01];%number of student entering into each class at time k
	sigma=0.02*np.asarray([0.0,3.6,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]) #University withdrawal rate (1-retained)for each class at time k
	beta=0.05*np.asarray(ones) #DFW rate for each class at time k (need to repeat)
	alpha=0.15*np.asarray(ones) #slowing factor to account for students taking less than 15 units per semester (need additional semester to complete class)
	lmbda=h*0.025*np.asarray([0,4,2,2,1,.5,.5,.5,.5,.5]) #could include "migrating" to allow calculation of grad in and out of COE

	return markovModel

def cohortTest(incomingStudents):
	#Do the training calculations in here
	#data = request.POST.get('data')
	incomingStudents = int(incomingStudents)

	##Inputs
	n = 8 #number of semesters in road map
	k = 15 #number of semesters to model
	p = 0 #steady state trigger, if p=1 steady-state, p=0 only add students in year 1 
	h = 0 #college trigger, if h=1, only calc College, if =0, calc university
	q =0 #system shock trigger, if q=1, add shock semester 15, if q=0 just steady state

	#Calibration Factors:
	#incomingStudents = request.data.get('students')
	##Calibration factors for PSO
	ones=[0,1,1,1,1,1,1,1,1]
	COEUnits=[0,3.5,3.5,5,5,12,12,13,13]
	incoming=incomingStudents*np.asarray([0,1,0,0,0,0,0,0,0,0]) #[.47,0.01,.01,0.01,.47,0.01,.01,0.01];%number of student entering into each class at time k
	#LOAD PARAMETER MODEL
	#Department name, '4year graduation', maybe other things
	sigma=0.02*np.asarray([0.0,3.6,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]) #University withdrawal rate (1-retained)for each class at time k
	beta=0.05*np.asarray(ones) #DFW rate for each class at time k (need to repeat)
	alpha=0.15*np.asarray(ones) #slowing factor to account for students taking less than 15 units per semester (need additional semester to complete class)
	lmbda=h*0.025*np.asarray([0,4,2,2,1,.5,.5,.5,.5,.5]) #could include "migrating" to allow calculation of grad in and out of COE

	#Preallocate Matrices 
	time=np.linspace(0,k,k+1)
	time1=np.linspace(0,k-1,k)
	x=np.zeros((n+1, k+1),dtype=int)
	x_migration=np.zeros((n+1, k+1),dtype=int)
	x_DFW=np.zeros((n+1, k+1),dtype=int)
	x_slowed=np.zeros((n+1, k+1),dtype=int)
	x_Withdraw=np.zeros((n+1, k+1),dtype=int)
	x_advance=np.zeros((n+1, k+1),dtype=int)
	y=np.zeros((1, k+1),dtype=np.double)
	retained=np.zeros((1, k+1),dtype=int)
	graduated=np.zeros((1, k+1),dtype=int)
	number_of_units_attempted=np.zeros((1, k+1),dtype=int)
	number_of_units_DFWed=np.zeros((1, k+1),dtype=int)
	cohortretention=np.zeros((1, k+1),dtype=np.double)
	cohortpersistance=np.zeros((1, k+1),dtype=np.double)
	cohortgrad=np.zeros((1, k+1),dtype=np.double)


###STUDENT FLOW MODEL###
	for t in range(1, k+1): #TIME
		for s in range(1, n+1):
			if t <= 1:
				x[s,t]=x_advance[s-1,t-1]+incoming[s]+x_DFW[s,t-1]+x_slowed[s,t-1]
			else:
				x[s,t]=x_advance[s-1,t-1]+incoming[s]*(1-np.mod(t,1))*p+x_DFW[s,t-1]+x_slowed[s,t-1]

			x_Withdraw[s,t]=x[s,t]*(sigma[s])
			x_migration[s,t]=x[s,t]*(lmbda[s])*(1-sigma[s])
			x_DFW[s,t]=x[s,t]*(beta[s])*(1-lmbda[s])*(1-sigma[s])
			x_slowed[s,t]=x[s,t]*(alpha[s])*(1-sigma[s])*(1-beta[s])
			x_advance[s,t]=x[s,t]*(1-sigma[s])*(1-lmbda[s])*(1-beta[s])*(1-alpha[s])
		y[0,t]= np.sum(x[:,t]) #number_of_students_enrolled
		graduated[0,t]=np.sum(x_advance[n,1:t])
		number_of_units_attempted[0,t]=(1-h)*(np.sum(y[0,t])-np.sum(x_slowed[:,t]))*15+(h)*np.sum((x[:,t]-x_slowed[:,t])*np.transpose(COEUnits))
		number_of_units_DFWed[0,t]=(1-h)*np.sum(x_DFW[:,t]*15)+h*np.sum(x_DFW[:,t]*np.transpose(COEUnits))


###COHORT CALCULATIONS###
	if p <= 0:
		t = 0
		cohortretention[0,t]=y[0,t+1]/incoming[1]
		cohortpersistance[0,t]=y[0,t+1]/incoming[1]
		for t in range(1, k):
			cohortpersistance[0,t]=y[0,t+1]/incoming[1]
			cohortgrad[0,t]=graduated[0,t]/incoming[1]
			cohortretention[0,t]=(graduated[0,t]+y[0,t+1])/incoming[1]
		yr4gradrate=np.sum(x_advance[n,1:8])/incoming[1]*100      #in units of percent(%)
		yr6gradrate=np.sum(x_advance[n,1:12])/incoming[1]*100  #in units of percent(%)
		endgradrate=np.sum(x_advance[n,1:15])/incoming[1]*100  #in units of percent(%)
		averageunitsperstudent=np.sum(number_of_units_attempted)/np.sum(incoming)

###SHOCK CALCULATIONS###
	if q >= 1:
		time=np.linspace(0,k+k-1,k+k)
		COEUnits=[0,3.5,3.5,5,5,12,12,13,13]
		incoming=710*[0,1,0,0,0,0,0,0,0,0] #[.47,0.01,.01,0.01,.47,0.01,.01,0.01];%number of student entering into each class at time k
		sigma=0.02*[0,3.6,1,1,1,1,1,1,1,1] #University withdrawal rate (1-retained)for each class at time k
		beta=0.05*ones #DFW rate for each class at time k (need to repeat)
		alpha=0.0*ones #slowing factor to account for students taking less than 15 units per semester (need additional semester to complete class)
		lmbda=h*0.025*[0,4,2,2,1,.5,.5,.5,.5,.5] #could include "migrating" to allow calculation of grad in and out of COE

###shock student flow model###
		for t in range(k+2, k+k):  #time
			for s in range(2, n+1): #semesters
				x[s,t]=x_advance(s-1,t-1)+incoming(s)*(1-mod(t,2))*p+x_DFW(s,t-1)+x_slowed(s,t-1)
				x_Withdraw[s,t]=x(s,t)*(sigma(s))
				x_migration[s,t]=x(s,t)*(lmbda(s))*(1-sigma(s))
				x_DFW[s,t]=x(s,t)*(beta(s))*(1-lmbda(s))*(1-sigma(s))
				x_slowed[s,t]=x(s,t)*(alpha(s))*(1-sigma(s))*(1-beta(s))
				x_advance[s,t]=x(s,t)*(1-sigma(s))*(1-lmbda(s))*(1-beta(s))*(1-alpha(s))
        
			y[t]=sum(x[:,t]) #number_of_students_enrolled
			graduated[t]=sum(x_advance[n+1,1:t])
			number_of_units_attempted[t]=(1-h)*(y(t)-sum(x_slowed[:,t]))*15+(h)*sum((x[:,t]-x_slowed[:,t])*np.transpose(COEUnits)) ###NEED TO FIGURE OUT TRANSPOSE
			number_of_units_DFWed[t]=(1-h)*sum(x_DFW[:,t]*15)+h*sum(x_DFW[:,t]*np.transpose(COEUnits))

	graduating=x_advance[n-1,:]
	DataTime=[2,4,6,7,8,10,12]
	if h<=0: #college trigger, if h=1, only calc College, if =0, calc university
		y1=y;
		graduating1=graduating;
		number_of_units_attempted1=number_of_units_attempted;
	

	data = {'figure1':{'x-axis':time,'uGrad':(y[0,:],'yellow'), 'coeGrad':(graduating,'orange')},
            'figure2':{'x-axis':time, 'f1':(x[1,:],'purple'), 'f2':(x[2,:],'red'), 's1':(x[3,:],'blue'), 's2':(x[4,:],'yellow'), 'j1':(x[5,:],'#0048BA'), 'j2':(x[6,:],'Amber'), 'se1':(x[7,:],'#7C0A02'), 'se2':(x[8,:],'brown')},
            'figure3':{'x-axis':time, 'persistance':(cohortpersistance[0],'#E34234'), 'retention':(cohortretention[0],'red'), 'graduation':(cohortgrad[0],'GREEN')},
            'figure4':{'x-axis':time, '0-29units':((x[1,:]+x[2,:])/2,'pink'), '30-59units':((x[3,:]+x[4,:])/2,'purple'), '60-89units':((x[5,:]+x[6,:])/2,'#03C03C'), '90-119units':((x[7,:]+x[8,:])/2, '#666699')}}
	return data


