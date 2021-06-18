from django.db import models
from django.contrib.auth.models import User

class SeatPricing(models.Model):
	today_datetime = models.DateField(null=True, blank=True,\
						verbose_name='Date & Time')
	price_per_seat = models.FloatField(max_length=99999.9,blank=True,
						null=True,verbose_name='Price')
	total_seats = models.PositiveIntegerField(null=True, blank=True,
						verbose_name='Total Seats')
	active_status = models.BooleanField(default=1, verbose_name='Is Active')
	
	class Meta:
		verbose_name = 'Seat Pricing'
		verbose_name_plural = '		Seat Pricing'

	def _str_(self):
		return str(self.total_seats)

class BookedTicketHistory(models.Model):
	mobile = models.CharField(max_length=30, null=True,blank=True,
	    				verbose_name='Phone Number')
	no_of_tickets = models.PositiveIntegerField(null=True, blank=True,
						verbose_name='Number of Tickets')
	date_of_booking = models.DateTimeField(blank=True, null=True,
						verbose_name='Booking Date & Time')
	active_status = models.BooleanField(default=1, verbose_name='Is Active')
	created_at = models.DateTimeField(auto_now_add=True,
						verbose_name='Creation Date & Time')

	class Meta:
			verbose_name = 'Booked Ticket History'
			verbose_name_plural = 'Booked Ticket History'

	def __str__(self):
		return str(self.mobile)


class ReviewSystem(models.Model):
	user_name = models.CharField(max_length=100, null=True,blank=True,
	                     verbose_name='Name')
	user_mobile = models.CharField(max_length=30, null=True,blank=True,
	    				verbose_name='User Mobile Number')
	comments = models.TextField(null=True, blank=True, \
						verbose_name='Comments/Review')
	date_of_booking = models.DateTimeField(blank=True,
						null=True,verbose_name='Booking Date & Time')
	is_like = models.BooleanField(default=1, verbose_name='Is Liked')
	created_at = models.DateTimeField(auto_now_add=True,
						verbose_name='Creation Date & Time')

	class Meta:
			verbose_name = 'Review System'
			verbose_name_plural = 'Review System'

	def __str__(self):
		return str(self.user_mobile)
