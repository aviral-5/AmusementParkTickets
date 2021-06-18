from rest_framework.views import APIView
from django.db.models import Q
from django.contrib.auth import authenticate , login
from rest_framework.authtoken.models import Token
from UserManagement.models import UserProfile
from rest_framework_tracking.mixins import LoggingMixin
from generic_services.responses import exception_response,\
auth_response, custom_error_msg_response
from .auth_validate import *


class UserLogin(LoggingMixin,APIView):
	"""
	User authorization POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used to provide login service to admin user.

		Data Post: {

			"mobile"		:		"7777777777",	
			"password"  	: 		"123456"
		}

		Response: {

			"success"		: 		True,
			"message"		: 		"You're logged in successfully!!"
		}

	"""
	def post(self, request, format=None):
		try:
			data = request.data
			data_validation_check = data_validation(data)
			if data_validation_check == None:
				pass
			else:
				return data_validation_check
			check_integrity = data_integrity(data)
			if check_integrity == None:
				pass
			else:
				return check_integrity
			user_authenticate = authenticate(username=(data['mobile']),
										password=data['password'])
			if user_authenticate == None:
				msg= "Your account is not authenticated,\
					contact to admin!!"
				return custom_error_msg_response({
						"success"	:	False,
						"message"	:	msg
					})
			else:
				pass
			if user_authenticate and user_authenticate.is_active == True \
									and user_authenticate.is_staff==False\
									and user_authenticate.is_superuser == False:
				login(request,user_authenticate)
				token, created = Token.objects.get_or_create(user=user_authenticate)
				user_id = token.user_id
				return auth_response(token.key)
			else:
				msg="Account is not Active!!"
				return custom_error_msg_response({
						"success"	:	False,
						"message"	:	msg
					})
		except Exception as e:
			return exception_response(str(e))