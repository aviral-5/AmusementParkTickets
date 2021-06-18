from django.contrib import admin
from django.contrib.auth.models import User
from UserManagement.models import *
from django import forms
from datetime import datetime
from django.forms.utils import ErrorList
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

#Function to create Auth user
def user_create(mobile, password):
	user_creation = User.objects.create_user(username=mobile,password=password,
			 is_staff=False,
			 is_active=True,
			)
	return user_creation 

#Function to make active , deactive
def make_active(modeladmin, request, queryset):
	queryset.update(active_status='1',updated_at=datetime.now())
make_active.short_description = "Move Items to Active"

def make_deactive(modeladmin, request, queryset):
	queryset.update(active_status='0',updated_at=datetime.now())
make_deactive.short_description = "Move Items to Deactive"


class UserProfileAdmin(admin.ModelAdmin):
	exclude = ['active_status','created_at','updated_at',]

	list_filter = [
		'active_status',
		'user_type',
		('created_at', DateRangeFilter),
		('updated_at', DateRangeFilter)
		]

	search_fields = ['name','email','mobile']

	list_display = ['auth_user','user_type','name','mobile','active_status','created_at',]
	readonly_fields = [
			'auth_user',
			]
	actions = [make_active, make_deactive]

	list_per_page = 10

	def has_delete_permission(self, request, obj=None):
		return False

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_at = datetime.now()
			created = user_create(obj.mobile, obj.password)
			user_id = User.objects.get(id=created.id)
			mobile = created.username
			obj.auth_user = user_id
			obj.save() 
		else:
			obj.updated_at = datetime.now()
			obj.save()

admin.site.register(UserProfile,UserProfileAdmin)
