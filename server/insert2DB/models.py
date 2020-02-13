from django.db import models
from django.utils import timezone

class Array(models.Model):
	array_num = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	#std_dev = models.IntegerField(1)
	def __str__(self):
		return self.array_num
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
