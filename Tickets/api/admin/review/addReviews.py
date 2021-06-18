import dateutil.parser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
#Serializer for api
from rest_framework import serializers
from rest_framework_tracking.mixins import LoggingMixin
from Tickets.models import ReviewSystem
from generic_services.responses import add_response,edit_response,\
exception_response,custom_error_msg_response
from .review_validate import *
from datetime import datetime
from generic_services.decorators.usertype import review_check


class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = ReviewSystem
		fields = '__all__'

class AddReviews(LoggingMixin,APIView):
	"""
	Review Create POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used to create reviews by normal users.
		Special Instruction			: Send Normal User Token key while accessing this API. 
		
		Data Post: {

			"user_name"		  	:	"Test User",	
			"user_mobile"    	:   "1234567890",
			"comments"   		:   "it was good experience,great park",
			"date_of_booking"   :   "2021-06-18",
			"is_like"   		:   "1/0"

		}

		Response: {

			"success"		: 		True,
			"message"		: 		"Review added successfully!!"
		}

	"""
	permission_classes = (IsAuthenticated,)
	@review_check
	def post(self, request, format=None):
		try:
			data = request.data
			data_validation_check = data_validation(data)
			if data_validation_check == None:
				pass
			else:
				return data_validation_check
			booked_user = booked_tickets_check(data)
			if booked_user == None:
				pass
			else:
				return booked_user
			mobile_check = user_integrity(data)
			if mobile_check == None:
				pass
			else:
				return mobile_check
			date_of_booking = dateutil.parser.parse(data["date_of_booking"])
			if "row" in data:
				i = data["row"][0]
				update_data = {}
				update_data["user_name"] = data["user_name"]
				update_data["user_mobile"] = data["user_mobile"]
				update_data["comments"] = data["comments"]
				update_data["date_of_booking"] = date_of_booking
				update_data["is_like"] = data["is_like"]
				serializer = ReviewSerializer(i,data=update_data,partial=True)
				if serializer.is_valid():
					data_info = serializer.save()
					return edit_response("Review/Comments")
				else:
					msg = str(serializer.errors)
					return custom_error_msg_response(msg)
			else:
				data["date_of_booking"]=date_of_booking
				serializer = ReviewSerializer(data=data)
				if serializer.is_valid():
					data_info = serializer.save()
					return add_response("Review/Comments")
				else:
					msg = str(serializer.errors)
					return custom_error_msg_response(msg)
		except Exception as e:
			return exception_response(str(e))
			
			