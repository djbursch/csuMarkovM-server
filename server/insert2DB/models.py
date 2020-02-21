from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Class for saving the data from each school and department
class Data(models.Model):
	#GOING TO CHANGE THIS TO FileField when getting actual data
	data = models.CharField(max_length = 200)
	schoolName = models.TextField(max_length = 200)
	departmentName = models.TextField(max_length = 200)
	markovModel = models.CharField(max_length = 200)
	pubDate = models.DateTimeField('date published')
	def __str__(self):
		return self.data
	def was_published_recently(self):
		return self.pubDate >= timezone.now() - datetime.timedelta(days=1)

#MODEL FOR INVITE VERIFICATION
class Invite(models.Model):
	username = models.TextField(max_length = 200)
	password = models.TextField(max_length = 200)
	invitecode = models.CharField(max_length = 200)
	pubDate = models.DateTimeField('date published')

#CONSUMER ROLES
class DeptConsumer(User):
	class Meta:
		permissions = (("is_member", "can_view"),)

class CollegeConsumer(DeptConsumer):
    class Meta:
    	permissions = (("can_upload", "Friendly message"),)

class UnivConsumer(CollegeConsumer):
    class Meta:
    	permissions = (("can_view_school", "Friendly message"),)

class SystemConsumer(UnivConsumer):
	class Meta:
		permissions = (("can_view_all", "Friendly message"),)

# PROVIDER ROLES
class DeptProvider(DeptConsumer):
	class Meta:
		permissions = (("can_view_all", "Friendly message"),)

class CollegeProvider(DeptProvider):
	class Meta:
		permissions = (("can_view_all", "Friendly message"),)

class UnivProvider(CollegeProvider):
	class Meta:
		permissions = (("can_view_all", "Friendly message"),)

class SystemProvider(UnivProvider):
	class Meta:
		permissions = (("can_view_all", "Friendly message"),)

#PROJECT OWNERS
class Developer(SystemProvider):
	class Meta:
		permissions = (("can_view_all", "Friendly message"),)
