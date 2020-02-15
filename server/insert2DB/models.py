from django.db import models
from django.utils import timezone

#Class for saving the actual data from each school
class Data(models.Model):
	#GOING TO CHANGE THIS TO FileField when getting actual data
	data = models.CharField(max_length = 200)
	schoolName = models.TextField(max_length = 200)
	departmentName = models.TextField(max_length = 200)
	markovModel = models.IntegerField(null=True)
	pubDate = models.DateTimeField('date published')
	def __str__(self):
		return self.data
	def was_published_recently(self):
		return self.pubDate >= timezone.now() - datetime.timedelta(days=1)

