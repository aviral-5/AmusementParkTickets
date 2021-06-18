#for error handling
from generic_services.api_packages import *
from django.contrib.auth.models import User
import re 
from django.db.models import Q
from generic_services.responses import error_response
from UserManagement.models import UserProfile

def error_dict_intiatlize():
	err_message = {}
	err_message["user_type"] = None
	err_message["name"] = None
	err_message["email"] = None
	err_message["mobile"] = None
	err_message["password"] = None
	return err_message

#Data key validation check for all type of authorization
def data_validation(data):
	err_message = error_dict_intiatlize()
	if data["user_type"] != "1" and data["user_type"] != "2":
		err_message["user_type"] = "User Type is not valid!!"
	else:
		pass
	err_message["name"] = \
	validation_master_anything(data["name"], "Name",username_re,3,80)
	err_message["email"] = \
	validation_master_anything(data["email"],"Email",email_re,2,80)
	err_message["mobile"] = \
	validation_master_anything(data["mobile"],"Mobile",contact_re,10,10)
	err_message["password"] = \
	validation_master_anything(data["password"],"Password",pass_re,6,12)
	
	if any(err_message.values()) == True:
		return error_response(err_message)
	else:
		return None

#mobile & email integrity check
def user_integrity(data):
	err_message = error_dict_intiatlize()
	if "mobile" in data:
		user_check = User.objects.filter(~Q(id=data["auth_user"]),Q(username=data["mobile"]))
	else:
		user_check = User.objects.filter(Q(username=data["mobile"]))

	if user_check.count()==0:
		pass
	else:
		err_message["mobile"] = "It seems provided mobile number already exists!!"

	if "email" in data:
		email_check = UserProfile.objects.filter(~Q(auth_user=data["auth_user"]),Q(email=data["email"]))
	else:
		email_check = UserProfile.objects.filter(Q(email=data["email"]))
	if email_check.count()==0:
		pass
	else:
		err_message["email"] = "It seems provided email already exists!!"
	
	if any(err_message.values()) == True:
		return error_response(err_message)
	else:
		return None 
