from .models import Array

#This is where the matlab code is going to be translated
#Just created the pipeline so it's ready to receive data

def Oracle(array_id):
	array = Array.objects.get(id=array_id)
	print(array)
	return array
