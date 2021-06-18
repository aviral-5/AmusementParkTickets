from datetime import datetime,timedelta
import re
from django.db.models import Sum
import string
 
zero__re = r'[0]*$'
contact_re = r'[0-9]*$'
description_re = r"[a-zA-z0-9 ]{1,}[@%&$.,/\()!|'#* -]{0,}[a-zA-z.,#@%&$/\()|!'0-9 -;]{0,}$"
email_re = r'[a-zA-Z0-9]{1,}[._]{0,}[a-zA-Z0-9]{1,}[@]{1,1}[a-zA-Z0-9]{1,}[.]{1,1}[a-zA-Z ]{1,}$'
username_re = r'[a-zA-Z.0-9& ]{1,}[-_& ]*[a-zA-Z.0-9& ]{1,}$'
pass_re = r'[a-zA-Z0-9-#$%^&*@!+_></\| ():;]{1,}$'

def validate_anything(field_to_validate, reg_re, zero_re,minimum_len, field_name,max_length):
	a = ""
	if len(field_to_validate)>max_length:
		a = field_name + " field can'nt contain more than "+str(max_length)+" characters!!"
	else:
		pass
	if field_to_validate != "" and a == "":
		if "^" in field_to_validate:
			a = "Please enter valid " +  field_name + "!!"
		if field_to_validate != None and len(field_to_validate)<minimum_len:
			a = field_name + " field should contain at least " + str(minimum_len) + " characters!!"
		if field_to_validate != None and re.match(zero__re, field_to_validate)\
											  and len(field_to_validate)>minimum_len-1:
			a = "All zeros are not allowed in " +field_name +" field!!"
		if field_to_validate != None and not re.match(zero__re, field_to_validate)\
				and len(field_to_validate)>minimum_len-1 and not re.match(reg_re, field_to_validate):
			a = "Please enter valid " +  field_name + "!!"
	else:
		pass
	if a == "":
		pass
	else:
		return a


def validation_master_anything(key_to_validate, alert_field_name, reg_re, min_length,max_length):
	if key_to_validate==None or key_to_validate=="":
		response = "Please enter your " + alert_field_name +"!!"
	else:
		response = validate_anything(key_to_validate, reg_re, zero__re,
								 min_length, alert_field_name,max_length)
	if response == "":
		pass
	else:
		return response

def only_required(key_to_validate, alert_field_name):
	if key_to_validate==None or key_to_validate=="" or key_to_validate=="Null":
		only_response = "Please enter your " + alert_field_name +"!!"
	else:
		only_response = ""
	if only_response == "":
		pass
	else:
		return only_response
