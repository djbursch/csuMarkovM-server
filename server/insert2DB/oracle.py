from .models import Data
import numpy as np
import random as rm

#This is where the matlab code is going to be translated
#Just created the pipeline so it's ready to receive data

def Oracle(schoolName):
	data = Data.objects.get(schoolName=schoolName)
	print(data)
	return data
