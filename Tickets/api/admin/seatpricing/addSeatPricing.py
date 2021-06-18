from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
#Serializer for api
from rest_framework import serializers
from rest_framework_tracking.mixins import LoggingMixin
from Tickets.models import SeatPricing
from generic_services.responses import add_response, edit_response,\
exception_response,custom_error_msg_response
from .seatprice_validate import *
from generic_services.decorators.usertype import admin_user_check


class SeatPricingSerializer(serializers.ModelSerializer):
	class Meta:
		model = SeatPricing
		fields = '__all__'

class SeatPricingAddUpdate(LoggingMixin,APIView):
	"""
	Seat Pricing Create & Update POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used to create seat pricings.
		Special Instruction			: Send Token key while accessing this API. 
		
		Data Post: {

			"today_datetime"	:	"2021-06-17",	
			"price_per_seat"    :   "250",
			"total_seats"       :   "50"

		}

		Response: {

			"success"		: 		True,
			"message"		: 		"Seat Pricing for today is added successfully!!"
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
			user_check = user_integrity(data)
			if user_check == None:
				pass
			else:
				return user_check
			if "row" in data:
				i = data["row"][0]
				update_data = {}
				update_data["today_datetime"] = data["today_datetime"]
				update_data["price_per_seat"] = data["price_per_seat"]
				update_data["total_seats"] = data["total_seats"]
				update_data["active_status"] = 1
				serializer = SeatPricingSerializer(i,data=update_data,partial=True)
				if serializer.is_valid():
					data_info = serializer.save()
					return edit_response("Seat Pricing")
				else:
					msg = str(serializer.errors)
					return custom_error_msg_response(msg)
			else:
				data["today_datetime"]=data["today_datetime"]
				data["price_per_seat"]=data["price_per_seat"]
				data["total_seats"]=data["total_seats"]
				data["active_status"]=1
				serializer = SeatPricingSerializer(data=data)
				if serializer.is_valid():
					data_info = serializer.save()
					return add_response("Seat Pricing")
				else:
					msg = str(serializer.errors)
					return custom_error_msg_response(msg)
		except Exception as e:
			return exception_response(str(e))
			
			