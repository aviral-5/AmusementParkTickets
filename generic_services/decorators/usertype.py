from django.contrib.auth.models import User
from UserManagement.models import UserProfile
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.db.models import Q

#decorator for Admin usertype

def admin_user_check(function):
	def inner(func,func1):
		mutable = func1.POST._mutable
		func1.POST._mutable = True
		auth_user = func1.user
		admin_check = UserProfile.objects.filter(auth_user=auth_user,\
			user_type='0',active_status=1)
		if admin_check.count()==0:
			success = False
			msg = "Account does'nt belong to Admin User Account!!"
			return Response({
				"success":success,
				"message":msg
				}) 
		else:
			func1.data["query"] = admin_check
			func1.data["auth_user"] = auth_user.id
			return function(func,func1)
	return inner

#decorator for other usertype

def normal_user_check(function):
	def inner(func,func1):
		mutable = func1.POST._mutable
		func1.POST._mutable = True
		auth_user = func1.user
		user_check = UserProfile.objects.filter(auth_user=auth_user,\
			user_type='2',active_status=1)
		if user_check.count()==0:
			success = False
			msg = "Account does'nt belong to Normal User Account!!"
			return Response({
				"success":success,
				"message":msg
				}) 
		else:
			func1.data["query"] = user_check
			func1.data["auth_user"] = auth_user.id
			func1.data["registered_mobile"] = user_check[0].mobile

			return function(func,func1)
	return inner

#decorator for review check
def review_check(function):
	def inner(func,func1):
		mutable = func1.POST._mutable
		func1.POST._mutable = True
		auth_user = func1.user
		user_check = UserProfile.objects.filter(auth_user=auth_user,\
			user_type='2',active_status=1)
		if user_check.count()==0:
			success = False
			msg = "You're not authorized to give review only normal-users are allowed!!"
			return Response({
				"success":success,
				"message":msg
				}) 
		else:
			func1.data["query"] = user_check
			func1.data["auth_user"] = auth_user.id

			return function(func,func1)
	return inner
