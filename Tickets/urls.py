from django.urls import path
from .api.admin.seatpricing.addSeatPricing import SeatPricingAddUpdate
from .api.admin.seatpricing.totalTickets import TotalTicketsListing

from .api.admin.booktickets.bookTickets import BookingTickets

from .api.admin.review.addReviews import AddReviews
from .api.admin.review.allUsers import AllUsers


urlpatterns = [
	#end points for seat pricing api

	path('SeatPricingAddUpdate/',SeatPricingAddUpdate.as_view()),
	path('TotalTicketsListing/',TotalTicketsListing.as_view()),

	#end points for booking tickets api

	path('BookingTickets/',BookingTickets.as_view()),
	
	#end points for reviews api

	path('AddReviews/',AddReviews.as_view()),
	path('AllUsers/',AllUsers.as_view()),
	


]