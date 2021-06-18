from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
#Serializer for api
from rest_framework import serializers
from rest_framework_tracking.mixins import LoggingMixin
from UserManagement.models import UserProfile
from generic_services.responses import add_response,\
exception_response,custom_error_msg_response
from .userprofile_validate import *
from datetime import datetime
from generic_services.decorators.usertype import admin_user_check


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = '__all__'

class UserProfileCreate(LoggingMixin,APIView):
	"""
	User Profile Create POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used to create users profile.
		Special Instruction			: Send Token key while accessing this API. 
		
		Data Post: {

			"user_type"		  :	  "1/2",	
			"name"    		  :   "Test User",
			"email"           :   "user@gmail.com",
			"mobile"          :   "9999000000",
			"password"        :   "123456"

		}

		Response: {

			"success"		: 		True,
			"message"		: 		"User Profile is added successfully!!"
		}

	"""
	permission_classes = (IsAuthenticated,)
	@admin_user_check
	def post(self, request, format=None):
		try:
			data = request.data
			data_validation_check = data_validation(data)
			if data_validation_check == None:
				pass
			else:
				return data_validation_check
			check_integrity = user_integrity(data)
			if check_integrity == None:
				pass
			else:
				return check_integrity
			create_user = User.objects.create(username=data["mobile"],\
					is_staff=False,password=data["password"])
			data["auth_user"]=create_user.id
			serializer = ProfileSerializer(data=data)
			if serializer.is_valid():
				data_info = serializer.save()
				return add_response("User Profile")
			else:
				msg = str(serializer.errors)
				return custom_error_msg_response(msg)
		except Exception as e:
			return exception_response(str(e))
			
			