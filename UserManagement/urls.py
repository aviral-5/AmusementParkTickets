from django.urls import path
from .api.admin.addUserProfile import UserProfileCreate


urlpatterns = [
	path('UserProfileCreate/',UserProfileCreate.as_view()),
	
]