#for error handling
from generic_services.api_packages import *
from django.contrib.auth.models import User
import re 
from django.db.models import Q
from generic_services.responses import error_response
from Tickets.models import ReviewSystem,BookedTicketHistory
from datetime import datetime,date

def error_dict_intiatlize():
	err_message = {}
	err_message["user_name"] = None
	err_message["user_mobile"] = None
	err_message["comments"] = None
	err_message["date_of_booking"] = None
	err_message["is_like"] = None
	return err_message

#Data key validation check for all type of authorization
def data_validation(data):
	err_message = error_dict_intiatlize()
	err_message["user_name"] = \
		validation_master_anything(data["user_name"], "Name",username_re,3,80)
	err_message["user_mobile"] = \
		validation_master_anything(data["user_mobile"],"Mobile",contact_re,10,10)
	err_message["comments"] = \
		validation_master_anything(data["comments"],"Comments/Review",description_re,3,500)
	err_message["date_of_booking"] =\
		only_required(data["date_of_booking"],"Date of Booking")
	if data["is_like"] != 1 and data["is_like"] != 0:
		err_message["is_like"] = "Value is not set properly!!"
	else:
		pass
	if any(err_message.values()) == True:
		return error_response(err_message)
	else:
		return None

def booked_tickets_check(data):
	err_message = error_dict_intiatlize()
	review_check = BookedTicketHistory.objects.filter(mobile=data["user_mobile"])
	if review_check.count()==0:
		err_message["user_mobile"] = "Only users who've booked tickets, can review!!"
	else:
		pass
	if any(err_message.values()) == True:
		return error_response(err_message)
	else:
		return None 


#review updation 
def user_integrity(data):
	err_message = error_dict_intiatlize()
	review_check = ReviewSystem.objects.filter(user_mobile=data["user_mobile"])
	if review_check.count()==0:
		pass
	else:
		data["row"] = review_check
	if any(err_message.values()) == True:
		return error_response(err_message)
	else:
		return None 
