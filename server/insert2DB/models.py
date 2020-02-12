from django.db import models

# Create your models here.
class Array(models.Model):
	array_num = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
