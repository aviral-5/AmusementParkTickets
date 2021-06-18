#for error handling
from generic_services.api_packages import *
from django.contrib.auth.models import User
import re 
from django.db.models import Q
from generic_services.responses import error_response
from Tickets.models import SeatPricing
from datetime import datetime,date
from django.utils import timezone


def error_dict_intiatlize():
	err_message = {}
	err_message["today_datetime"] = None
	err_message["price_per_seat"] = None
	err_message["total_seats"] = None
	return err_message

#Data key validation check for all type of authorization
def data_validation(data):
	err_message = error_dict_intiatlize()
	try:
		data["price_per_seat"] = float(data["price_per_seat"])
	except Exception as e:
		err_message["price_per_seat"] = "Pricing per Seat value is not valid!!"
	try:
		data["total_seats"] = int(data["total_seats"])
	except Exception as e:
		err_message["total_seats"] = "Total Seats value is not valid!!"
	err_message["today_datetime"] =\
		only_required(data["today_datetime"],"Today's Date")	
	if any(err_message.values()) == True:
		return error_response(err_message)
	else:
		return None

#date integrity check
def user_integrity(data):
	err_message = error_dict_intiatlize()
	check_record = SeatPricing.objects.filter(today_datetime__gte=timezone.now().date())
	if check_record.count()==0:
		pass
	else:
		data["row"] = check_record
	if any(err_message.values()) == True:
		return error_response(err_message)
	else:
		return None 
