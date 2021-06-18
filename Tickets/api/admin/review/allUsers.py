from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_tracking.mixins import LoggingMixin
from Tickets.models import ReviewSystem
from datetime import datetime
from generic_services.responses import customized_data_response, exception_response
from generic_services.decorators.usertype import admin_user_check
	

class AllUsers(LoggingMixin,APIView):
	"""
	Liked and Disliked User GET API

		Authorization Required		: Yes
		Service Usage & Description	: This Api is used to users who liked & disliked park.
	"""
	permission_classes = (IsAuthenticated,)
	@admin_user_check
	def get(self, request, format=None):
		try:
			data = request.data
			record = ReviewSystem.objects.all()
			result = []
			if record.count()==0:
				result=[]
			else:
				total_likes = record.filter(is_like=1).count()
				total_dislikes = record.filter(is_like=0).count()
				for i in record:
					data_dict = {}
					data_dict["name"] = i.user_name
					data_dict["mobile"] = i.user_mobile
					data_dict["date_of_booking"] = i.date_of_booking.strftime('%d-%m-%Y %I:%M %p')
					data_dict["liked"] = i.is_like

					result.append(data_dict)
			return customized_data_response(result,total_likes,total_dislikes)
		except Exception as e:
			return exception_response(str(e))