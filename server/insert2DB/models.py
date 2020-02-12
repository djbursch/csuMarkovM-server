from django.db import models
from django.utils import timezone

# Create your models here.
class Array(models.Model):
	array_num = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.array_num
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
