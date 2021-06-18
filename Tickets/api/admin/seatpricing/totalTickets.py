from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_tracking.mixins import LoggingMixin
from Tickets.models import SeatPricing
from django.utils import timezone
from generic_services.responses import data_response, exception_response
from generic_services.decorators.usertype import admin_user_check
	

class TotalTicketsListing(LoggingMixin,APIView):
	"""
	Total Ticket of Today GET API

		Authorization Required		: Yes
		Service Usage & Description	: This Api is used to serve total tickets by today.
	"""
	permission_classes = (IsAuthenticated,)
	@admin_user_check
	def get(self, request, format=None):
		try:
			data = request.data
			record = SeatPricing.objects.filter(active_status=1,\
				today_datetime__gte=timezone.now().date())
			result = []
			if record.count()==0:
				result=[]
			else:
				for i in record:
					data_dict = {}
					data_dict["today_date"] = i.today_datetime
					data_dict["price_per_seats"] = i.price_per_seat
					data_dict["total_seats"] = i.total_seats
					data_dict["total_tickets"] = i.total_seats
					result.append(data_dict)
			return data_response(result)
		except Exception as e:
			return exception_response(str(e))