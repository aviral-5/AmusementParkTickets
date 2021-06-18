#for error handling
from generic_services.api_packages import *
from django.contrib.auth.models import User
import re 
from django.db.models import Q
from generic_services.responses import error_response
from UserManagement.models import UserProfile

def error_dict_intiatlize():
	err_message = {}
	err_message["mobile"] = None
	err_message["password"] = None
	return err_message

#Data key validation check for all type of authorization
def data_validation(data):
	err_message = error_dict_intiatlize()
	err_message["mobile"] = \
	validation_master_anything(data["mobile"],"Mobile",contact_re,10,10)
	err_message["password"] = \
	validation_master_anything(data["password"],"Password",pass_re,6,12)
	if any(err_message.values()) == True:
		return error_response(err_message)
	else:
		return None

def data_integrity(data):
	err_message = error_dict_intiatlize()
	if "mobile" in data and "password" in data:
		user_check = UserProfile.objects.filter(mobile=data['mobile'],\
				password=data['password'],active_status=1)
		if user_check.count()==1:
			pass
		else:
			err_message["user"] = "Account is nor registered or usertype is invalid!!"
	else:
		pass
	if any(err_message.values()) == True:
		return error_response(err_message)
	else:
		return None