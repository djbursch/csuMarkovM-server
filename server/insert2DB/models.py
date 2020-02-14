from django.db import models
from django.utils import timezone

#Class for saving the actual data from each school
class Data(models.Model):
	#GOING TO CHANGE THIS TO FileField when getting actual data
	schoolData = models.CharField(max_length = 200)
	schoolName = models.TextField(max_length = 200)
	departmentName = models.TextField(max_length = 200)
	pubDate = models.DateTimeField('date published')
	def __str__(self):
		return self.schoolData
	def was_published_recently(self):
		return self.pubDate >= timezone.now() - datetime.timedelta(days=1)

#Skeleton for when we need to start saving models for each school and department
class markovModel(models.Model):
	schoolName = models.TextField(max_length = 200)
	departmentName = models.TextField(max_length = 200)
	pubDate = models.DateTimeField('date published')
	weights = models.IntegerField()
	def __str__(self):
		return self.weights
	def was_published_recently(self):
		return self.pubDate >= timezone.now() - datetime.timedelta(days=1)
