from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from improved_permissions.mixins import RoleMixin

#Class for saving the data from each school and department
class Data(models.Model):
	#GOING TO CHANGE THIS TO FileField when getting actual data
	data = models.CharField(max_length = 200)
	schoolName = models.TextField(max_length = 200)
	departmentName = models.TextField(max_length = 200)
	#markovModel = models.CharField(max_length = 200)
	pubDate = models.DateTimeField('date published')
	def __str__(self):
		return self.data
	def was_published_recently(self):
		return self.pubDate >= timezone.now() - datetime.timedelta(days=1)
	class Meta:
		permissions = (
				("can_write_sys", "Can write sys"),
				("can_write_uni", "Can write uni"),
				("can_write_clg", "Can write clg"),
				("can_write_dpt", "Can write dpt"),
				#("can_read_dpt", "Can read dpt"),
				#("can_read_clg", "Can read clg"),
				#("can_read_uni", "Can read uni"),
				#("can_read_sys", "Can read sys")
				)
	#class RoleOptions:
        # permission_parents = ['my_library'] maybe this will be useful when we have 2 dbs...
		#unique_together = True

class ModelData(models.Model):
	schoolName = models.TextField(max_length = 200)
	departmentName = models.TextField(max_length = 200)
	userProvider = models.TextField(max_length = 200)
	typeOfData = models.TextField(max_length = 200)
	sigma = models.IntegerField()
	alpha = models.IntegerField()
	beta = models.IntegerField()
	lmbda = models.IntegerField()
	pubDate = models.DateTimeField('date published')
	def was_published_recently(self):
		return self.pubDate >= timezone.now() - datetime.timedelta(days=1)
	class Meta:
		permissions = (
				("can_read_dpt", "Can read dpt"),
				("can_read_clg", "Can read clg"),
				("can_read_uni", "Can read uni"),
				("can_read_sys", "Can read sys")
				)
	#class RoleOptions:
        # permission_parents = ['my_library'] maybe this will be useful when we have 2 dbs...
		#unique_together = True




#class predictionType(models.Model):
	'''
	schoolName
	departmentName = 'CECS'
	systemName = 'CSU'
	userProvider
	typeOfData = '4 year graduation'
	sigma
	alpha
	beta
	lmbda
	'''
	#greek letters go here

#MODEL FOR INVITE VERIFICATION
'''
class Invite(models.Model):
	username = models.TextField(max_length = 200)
	password = models.TextField(max_length = 200)
	invitecode = models.CharField(max_length = 200)
	pubDate = models.DateTimeField('date published')

# CONSUMER ROLES
class DepartmentConsumer(models.Model):
	class Meta:
		permissions = (("can_read_dpt", "Can read dpt"),)

class CollegeConsumer(models.Model):
    class Meta:
    	permissions = (("can_read_clg", "Can read clg"),
    					("can_read_dpt", "Can read dpt"),)

class UniversityConsumer(models.Model):
    class Meta:
    	permissions = (("can_read_uni", "Can read uni"),
    					("can_read_clg", "Can read clg"),
    					("can_read_dpt", "Can read dpt"),)

class SystemConsumer(models.Model):
	class Meta:
		permissions = (("can_read_sys", "Can read sys"),
						("can_read_uni", "Can read uni"),
    					("can_read_clg", "Can read clg"),
    					("can_read_dpt", "Can read dpt"),)

# PROVIDER ROLES
class DepartmentProvider(models.Model):
	class Meta:
		permissions = (("can_write_dpt", "Can write dpt"),
						("can_read_dpt", "Can read dpt"),)

class CollegeProvider(models.Model):
	class Meta:
		permissions = (("can_write_clg", "Can write clg"),
						("can_write_dpt", "Can write dpt"),
						("can_read_dpt", "Can read dpt"),
						("can_read_clg", "Can read clg"),)

class UniversityProvider(models.Model):
	class Meta:
		permissions = (("can_write_uni", "Can write uni"),
						("can_write_clg", "Can write clg"),
						("can_write_dpt", "Can write dpt"),
						("can_read_dpt", "Can read dpt"),
						("can_read_clg", "Can read clg"),
						("can_read_uni", "Can read uni"),)

class SystemProvider(models.Model):
	class Meta:
		permissions = (("can_write_sys", "Can write sys"),
						("can_write_uni", "Can write uni"),
						("can_write_clg", "Can write clg"),
						("can_write_dpt", "Can write dpt"),
						("can_read_dpt", "Can read dpt"),
						("can_read_clg", "Can read clg"),
						("can_read_uni", "Can read uni"),
						("can_read_sys", "Can read sys"),)

#PROJECT OWNERS
class Developer(models.Model):
	class Meta:
		permissions = (("can_view_all", "Can view all"),)
'''
