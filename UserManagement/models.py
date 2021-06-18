from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	auth_user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, 
		blank=True,related_name ='UserProfile_auth_user')
	user_type = models.CharField(max_length=50, choices=[
						('0','Admin'), 
						('1','Ticket-Counter'),
						('2','Normal-User'),
						],verbose_name='User Types',null=True,blank=True)
	name = models.CharField(max_length=100, null=True,blank=True,
	                      verbose_name='Name')
	email =  models.EmailField(max_length=100,null=True,blank=True,
		unique=True,verbose_name='Email')
	mobile = models.CharField(max_length=30, null=True,blank=True,
	    verbose_name='Phone Number')
	password = models.CharField(max_length=100, null=True,blank=True,
	                      verbose_name='Password')
	active_status = models.BooleanField(default=1,
							verbose_name="Is Active")
	created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True, 
							verbose_name='Creation Date')
	updated_at = models.DateTimeField(blank=True, null=True,
						verbose_name='Updation Date')

	class Meta:
		verbose_name='User Profile'
		verbose_name_plural=' User Profile'

	def _str_(self):
		return str(self.auth_user)