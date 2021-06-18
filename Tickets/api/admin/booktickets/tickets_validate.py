#for error handling
from generic_services.api_packages import *
from django.contrib.auth.models import User
import re 
from django.db.models import Q
from generic_services.responses import error_response
from UserManagement.models import UserProfile
from Tickets.models import SeatPricing,BookedTicketHistory
from django.utils import timezone
from datetime import datetime,date

def error_dict_intiatlize():
	err_message = {}
	err_message["mobile"] = None
	err_message["no_of_tickets"] = None
	err_message["date_of_booking"] = None
	return err_message

#Data key validation check for all type of authorization
def data_validation(data):
	err_message = error_dict_intiatlize()
	err_message["mobile"] = \
	validation_master_anything(data["mobile"],"Mobile",contact_re,10,10)
	err_message["no_of_tickets"] = \
	validation_master_anything(str(data["no_of_tickets"]),"No of Tickets",contact_re,1,80)
	err_message["date_of_booking"] =\
	only_required(data["date_of_booking"],"Date of Booking")	
	if any(err_message.values()) == True:
		return error_response(err_message)
	else:
		return None

#availability of tickets
def available_tickets_today(data):
	err_message = error_dict_intiatlize()
	ticket_check = SeatPricing.objects.filter(active_status=1,\
				today_datetime__gte=timezone.now().date())
	if ticket_check.count()==0:
		err_message["no_of_tickets"] = "All tickets are already booked, please check again!!"
	else:
		total_tickets=ticket_check[0].total_seats
		
		if int(data["no_of_tickets"])>int(total_tickets):
			err_message["no_of_tickets"] = "Only "+str(total_tickets)+" tickets are left for today!!"
		else:
			pass
	if any(err_message.values()) == True:
		return error_response(err_message)
	else:
		return None 

#availability of tickets
def mobile_integrity(data):
	err_message = error_dict_intiatlize()
	ticket_check = UserProfile.objects.filter(mobile=data["mobile"],auth_user=data["auth_user"])
	if ticket_check.count()==0:
		err_message["mobile"] = "Mobile Number is not valid, please check again!!"
	else:
		pass
	if any(err_message.values()) == True:
		return error_response(err_message)
	else:
		return None 
