from django.contrib import admin
from django.contrib.auth.models import User
from Tickets.models import *
from UserManagement.admin import make_active, make_deactive
from django import forms
from datetime import datetime
from django.forms.utils import ErrorList


class SeatPricingAdmin(admin.ModelAdmin):
	exclude = ['active_status']

	list_filter = [
		'active_status',
		]
	search_fields = ['total_seats',]

	list_display = ['today_datetime','price_per_seat','total_seats','active_status',]

	actions = [make_active, make_deactive]

	list_per_page = 10

	def has_delete_permission(self, request, obj=None):
		return False

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_at = datetime.now()
		else:
			obj.updated_at = datetime.now()
		obj.save()

admin.site.register(SeatPricing,SeatPricingAdmin)

class BookedTicketHistoryAdmin(admin.ModelAdmin):
	exclude = ['active_status']

	list_filter = [
		'active_status',
		]
	search_fields = ['mobile','no_of_tickets']

	list_display = ['mobile','no_of_tickets','date_of_booking','active_status','created_at']

	actions = [make_active, make_deactive]

	list_per_page = 10

	def has_delete_permission(self, request, obj=None):
		return False

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_at = datetime.now()
		else:
			obj.updated_at = datetime.now()
		obj.save()

admin.site.register(BookedTicketHistory,BookedTicketHistoryAdmin)

class ReviewSystemAdmin(admin.ModelAdmin):
	list_filter = [
		'is_like',
		]
	search_fields = ['mobile','no_of_tickets']

	list_display = ['user_name','user_mobile','comments','date_of_booking','is_like','created_at']
	list_per_page = 10

	def has_delete_permission(self, request, obj=None):
		return False

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_at = datetime.now()
		else:
			obj.updated_at = datetime.now()
		obj.save()

admin.site.register(ReviewSystem,ReviewSystemAdmin)
