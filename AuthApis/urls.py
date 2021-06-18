from django.urls import path
from .login import UserLogin

urlpatterns = [

	path('UserLogin/',UserLogin.as_view()),

]