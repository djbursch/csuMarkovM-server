from django.shortcuts import render
from .models import Array

def Oracle(array_id):
	array = Array.objects.get(id=array_id)
	print(array)
	return array
