from django.db import models
from django.utils import timezone

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
