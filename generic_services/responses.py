from rest_framework.response import Response


def add_response(title):
	return Response({
				"success"	: 	True, 
				"message"	: 	title+" is created successfully!!"
				})

def custom_success_msg_response(msg):
	return Response({
				"success"	: 	True, 
				"message"	: 	msg
				})

def edit_response(title):
	return Response({
				"success"	: 	True, 
				"message"	: 	title+" is updated successfully!!"
				})


def data_response(final_result):
	return Response({
				"success"	: 	True, 
				"data"		: 	final_result,
				})	

def customized_data_response(final_result,count1,count2):
	return Response({
				"success"			: 	True, 
				"total_likes"		:   count1,
				"total_dislikes"	:   count2,
				"data"				: 	final_result
				})	

def custom_error_msg_response(msg):
	return Response({
				"success"	:	False,
				"message"	:	msg
		})


def exception_response(e):
	return Response({
				"success"	: 	False, 
				"message"	: 	"Error happened: "+e+" !!"
				})

def error_response(err_message):
	return Response({
			"success"	: 	False,
			"error" 	:	err_message,
			"message" 	: 	"Please correct listed errors!!"
		})
	
def auth_response(token):
	return Response({
		"success"	:	True,
		"token"		:	token,
		"message"	:	"You are logged in now!!"
		})

