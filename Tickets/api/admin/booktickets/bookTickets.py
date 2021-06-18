import dateutil.parser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
#Serializer for api
from rest_framework import serializers
from rest_framework_tracking.mixins import LoggingMixin
from Tickets.models import SeatPricing,BookedTicketHistory
from generic_services.responses import custom_success_msg_response,\
exception_response,custom_error_msg_response
from .tickets_validate import *
from datetime import datetime
from generic_services.decorators.usertype import normal_user_check


class TicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookedTicketHistory
		fields = '__all__'

class BookingTickets(LoggingMixin,APIView):
	"""
	Book Tickets POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used to book tickets by normal users.
		Special Instruction			: Send Normal User Token key while accessing this API. 
		
		Data Post: {

			"mobile"		  	:	"1234567890",	
			"no_of_tickets"    	:   "2",
			"date_of_booking"   :   "2021-06-18"
		}

		Response: {

			"success"		: 		True,
			"message"		: 		"Tickets booked successfully!!"
		}

	"""
	permission_classes = (IsAuthenticated,)
	@normal_user_check
	def post(self, request, format=None):
		try:
			data = request.data
			data_validation_check = data_validation(data)
			if data_validation_check == None:
				pass
			else:
				return data_validation_check
			mobile_check = mobile_integrity(data)
			if mobile_check == None:
				pass
			else:
				return mobile_check
			available_tickets = available_tickets_today(data)
			if available_tickets == None:
				pass
			else:
				return available_tickets
			data["mobile"]=data["mobile"]
			data["no_of_tickets"]=data["no_of_tickets"]
			date_of_booking = dateutil.parser.parse(data["date_of_booking"])
			data["date_of_booking"]=date_of_booking
			data["active_status"]=1
			serializer = TicketSerializer(data=data)
			if serializer.is_valid():
				data_info = serializer.save()
				record = SeatPricing.objects.filter(today_datetime__gte=timezone.now().date())
				i=record[0]
				record.update(total_seats=i.total_seats-int(data["no_of_tickets"]))
				msg = "Your tickets are booked successfully!!"
				return custom_success_msg_response(msg)
			else:
				msg = str(serializer.errors)
				return custom_error_msg_response(msg)
		except Exception as e:
			return exception_response(str(e))
			
			