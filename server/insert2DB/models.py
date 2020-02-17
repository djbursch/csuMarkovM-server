from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Class for saving the data from each school and department
class Data(models.Model):
	#GOING TO CHANGE THIS TO FileField when getting actual data
	data = models.CharField(max_length = 200)
	schoolName = models.TextField(max_length = 200)
	departmentName = models.TextField(max_length = 200)
	markovModel = models.IntegerField()
	pubDate = models.DateTimeField('date published')
	def __str__(self):
		return self.data
	def was_published_recently(self):
		return self.pubDate >= timezone.now() - datetime.timedelta(days=1)

#All the different users
class Teacher(User):
	class Meta:
		permissions = (("is_member", "can_view"),)

class dptAdmin(Teacher):
    class Meta:
    	permissions = (("can_upload", "Friendly message"),)

class Dean(dptAdmin):
    class Meta:
    	permissions = (("can_view_school", "Friendly message"),)

class Chancellor(Dean):
	class Meta:
		permissions = (("can_view_all", "Friendly message"),)
