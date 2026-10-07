#####################################################################
import os, requests, json, csv, subprocess, yaml, time, re
from datetime import datetime
from dateutil.relativedelta import relativedelta
#####################################################################

# 2021-11

android_api_object = {
	"api_key": "REDACTED_API_KEY",
	"app_analysis_premium": {
		"engagement":{
			"describe":{
				"url":"https://api.similarweb.com/v4/data-ai/engagement/describe?api_key=REDACTED_API_KEY",
				"region":"US",
				"granularity": "Monthly",
				"start_date": "2022-08",
				"end_date": "2023-10",
				"period":14
			},
			"monthly_active_users":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/mau?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
			},
			"install_base":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/install-base?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
			},
			"total_time":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/total-time?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
			},
			"total_sessions":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/total-sessions?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
			},
			"average_monthly_user_sessions":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/average-monthly-user-sessions?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
			},
			"average_monthly_user_time_spent":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/average-monthly-user-time-spent?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
			},
			"average_session_length":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/average-session-length?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
			},
			"open_rate":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/open-rate?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
			}
		},
		"retention":{
			"describe":{
				"url":"https://api.similarweb.com/v4/data-ai/retention-d30/describe?api_key=REDACTED_API_KEY",
				"region":"US",
				"granularity": "Monthly",
				"start_date": "2022-07",
				"end_date": "2023-09",
				"period":24
			},
			"day_30_retention":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/retention?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
			}
		},
		"affinity":{
			"describe":{
				"url":"https://api.similarweb.com/v4/data-ai/audience-interests/describe?api_key=REDACTED_API_KEY",
				"region":"US",
				"granularity": "Monthly",
				"start_date": "2022-08",
				"end_date": "2023-10",
				"period":14
			},
			"affinity":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/audience-interests?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json&limit=100"
			}
		},
		"downloads":{
			"describe":{
				"url":"https://api.similarweb.com/v4/data-ai/engagement/downloads/describe?api_key=REDACTED_API_KEY",
				"region":"World",
				"granularity": "Monthly",
				"start_date": "2022-08",
				"end_date": "2023-10",
				"period":14
			},
			"downloads":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/downloads?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=world&granularity=monthly&format=json"
			}
		},
		"audience":{
			"describe":{
				"url":"https://api.similarweb.com/v4/data-ai/demographics/describe?api_key=REDACTED_API_KEY",
				"region":"US",
				"granularity": "Monthly",
				"start_date": "2022-08",
				"end_date": "2023-10",
				"period":14
			},
			"app_demographics_age":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/demographics/age?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&format=json"
			},
			"app_demographics_gender":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/demographics/gender?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&format=json"
			}
		},
	}
}








apple_api_object = {
	"api_key": "REDACTED_API_KEY",
	"app_analysis_premium": {
		"engagement":{
			"describe":{
				"url":"https://api.similarweb.com/v4/data-ai/engagement/describe?api_key=REDACTED_API_KEY",
				"region":"US",
				"granularity": "Monthly",
				"start_date": "2022-04",
				"end_date": "2023-06",
				"period":14
			},
			"monthly_active_users":{
				"url": "https://api.similarweb.com/v4/data-ai/Apple/app_id/mau?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=iPhone&format=json"
			},
			"install_base":{
				"url": "https://api.similarweb.com/v4/data-ai/Apple/app_id/install-base?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=iPhone&format=json"
			},
			"total_time":{
				"url": "https://api.similarweb.com/v4/data-ai/Apple/app_id/total-time?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=iPhone&format=json"
			},
			"total_sessions":{
				"url": "https://api.similarweb.com/v4/data-ai/Apple/app_id/total-sessions?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=iPhone&format=json"
			},
			"average_monthly_user_sessions":{
				"url": "https://api.similarweb.com/v4/data-ai/Apple/app_id/average-monthly-user-sessions?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=iPhone&format=json"
			},
			"average_monthly_user_time_spent":{
				"url": "https://api.similarweb.com/v4/data-ai/Apple/app_id/average-monthly-user-time-spent?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=iPhone&format=json"
			},
			"average_session_length":{
				"url": "https://api.similarweb.com/v4/data-ai/Apple/app_id/average-session-length?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=iPhone&format=json"
			},
			"open_rate":{
				"url": "https://api.similarweb.com/v4/data-ai/Apple/app_id/open-rate?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=iPhone&format=json"
			}
		},
		"affinity":{
			"describe":{
				"url":"https://api.similarweb.com/v4/data-ai/audience-interests/describe?api_key=REDACTED_API_KEY",
				"region":"US",
				"granularity": "Monthly",
				"start_date": "2022-04",
				"end_date": "2023-06",
				"period":14
			},
			"affinity":{
				"url": "https://api.similarweb.com/v4/data-ai/Apple/app_id/audience-interests?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=iPhone&format=json&limit=100"
			}
		}
	}
}



#############################################################
# RETENTION THROWS AN INTERNAL SERVER ERROR #
#############################################################
# apple_api_object = {
# 	"api_key": "REDACTED_API_KEY",
# 	"app_analysis_premium": {
# 		"engagement":{
# 			"describe":{
# 				"url":"https://api.similarweb.com/v4/data-ai/engagement/describe?api_key=REDACTED_API_KEY",
# 				"region":"US",
# 				"granularity": "Monthly",
# 				"start_date": "2022-04",
# 				"end_date": "2023-06",
# 				"period":14
# 			},
# 			"monthly_active_users":{
# 				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/mau?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
# 			},
# 			"install_base":{
# 				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/install-base?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
# 			},
# 			"total_time":{
# 				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/total-time?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
# 			},
# 			"total_sessions":{
# 				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/total-sessions?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
# 			},
# 			"average_monthly_user_sessions":{
# 				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/average-monthly-user-sessions?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
# 			},
# 			"average_monthly_user_time_spent":{
# 				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/average-monthly-user-time-spent?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
# 			},
# 			"average_session_length":{
# 				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/average-session-length?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
# 			},
# 			"open_rate":{
# 				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/open-rate?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
# 			}
# 		},
# 		"retention":{
# 			"describe":{
# 				"url":"https://api.similarweb.com/v4/data-ai/retention-d30/describe?api_key=REDACTED_API_KEY",
# 				"region":"US",
# 				"granularity": "Monthly",
# 				"start_date": "2022-03",
# 				"end_date": "2023-05",
# 				"period":24
# 			},
# 			"day_30_retention":{
# 				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/retention?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
# 			}
# 		},
# 		"affinity":{
# 			"describe":{
# 				"url":"https://api.similarweb.com/v4/data-ai/audience-interests/describe?api_key=REDACTED_API_KEY",
# 				"region":"US",
# 				"granularity": "Monthly",
# 				"start_date": "2022-04",
# 				"end_date": "2023-06",
# 				"period":14
# 			},
# 			"affinity":{
# 				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/audience-interests?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json&limit=100"
# 			}
# 		}
# 	}
# }

#####################################################################

def diff_month(end_date, start_date):
	return (end_date.year - start_date.year) * 12 + end_date.month - start_date.month

# CREATE ANOTHER VERSION IF THERE ARE GRANULARITIES OTHERE THAN "MONTHLY"
def get_end_month(period):
	current_month 	= str(datetime.now().month)
	current_year 	= str(datetime.now().year)
	if len(current_month) == 1:
		current_month = "0"+current_month
	end_month = datetime.strptime(str(current_year)+"-"+str(current_month), "%Y-%m")
	return end_month - relativedelta(months=2)

def get_start_month(start_month, period):
	end_date 	= start_month - relativedelta(months=period)
	end_month 	= str(end_date.month)	
	end_year 	= str(end_date.year)	
	if len(end_month) == 1:
		end_month = "0"+end_month
	end_date	= end_year +"-"+end_month
	return end_date

def end_month_add_zero(end_month_string):
	a = end_month_string.split("-")
	b = str(a[0])
	c = str(a[1])
	if len(c) == 1:
		c = "0"+c
	return b+"-"+c

#####################################################################

# def format_api_object_periods():
# 	for a in api_object:
# 		if type(api_object[a]) is not str:
# 			for b in api_object[a]:
# 				if type(api_object[a][b]) is not str:
# 					for c in api_object[a][b]:
# 						#######################
# 						end_month 	= get_end_month(api_object[a][b]["describe"]["period"])
# 						start_month = get_start_month(end_month, api_object[a][b]["describe"]["period"])
# 						end_month 	= str(end_month.year)+"-"+str(end_month.month)
# 						end_month 	= end_month_add_zero(end_month)						
# 						#######################
# 						print("format_api_object: end_month: ", end_month)
# 						print("format_api_object: start_month: ", start_month)
# 						#######################
# 						api_object[a][b]["describe"]["end_date"] 	= end_month
# 						api_object[a][b]["describe"]["start_date"] 	= start_month
# 						#######################
# 						if type(api_object[a][b][c]) is not str:
# 							for d in api_object[a][b][c]:
# 								if d == "url":
# 									api_object[a][b][c][d] = api_object[a][b][c][d].replace("similarweb_api_key", str(api_object["api_key"])).replace("user_end_date", str(end_month)).replace("user_start_date", str(start_month))
# 	print(api_object)


def format_api_object_dates(object_item, api_response):
	# print("format_api_object_dates: object_item['describe']: ", object_item["describe"])
	# print("format_api_object_dates: object_item['describe']['region']: ", object_item["describe"]["region"])
	object_dates = api_response["response"]["countries"][str(object_item["describe"]["region"].lower())]
	for a in object_dates:
		print("format_api_object_dates: a: ", a)
		print("format_api_object_dates: object_dates[a]: ", object_dates[a])
		print("format_api_object_dates: object_item['describe'][str(a)]: before: ", object_item["describe"][str(a)])
		object_item["describe"][str(a)] = object_dates[a]
		print("format_api_object_dates: object_item['describe'][str(a)]: after:", object_item["describe"][str(a)])
		print("format_api_object_dates: ****************************************************")
		print("format_api_object_dates: ****************************************************")


def format_api_object_describe_endpoint(api_object):
	for a in api_object:
		if type(api_object[a]) is not str:
			for b in api_object[a]:
				if type(api_object[a][b]) is not str:
					#######################

					#######################
					#######################
					#######################
						# api_object[a][b]["describe"]["url"] = api_object[a][b]["describe"]["url"].replace("similarweb_api_key", str(api_object["api_key"]))
						# api_response 						= call_json(api_object[a][b]["describe"]["url"])

						# if api_response.status_code == 200:	
						# 	#######################
						# 	print("format_api_object: api_response.status_code: !!SUCCESS!!: ", api_response.status_code)
						# 	print("format_api_object: api_response.status_code: !!SUCCESS!!: ", api_response.status_code)
						# 	#######################
						# 	# print("format_api_object: api_response: ", api_response)
						# 	#######################
						# 	formatted_response 	= format_json(api_response)
						# 	# print("format_api_object: formatted_response: ", formatted_response)
						# 	#######################
						# 	print("format_api_object: api_object[a][b]: before: ", api_object[a][b])
						# 	format_api_object_dates(api_object[a][b], formatted_response)
						# 	print("format_api_object: api_object[a][b]: after: ", api_object[a][b])
						# 	print("format_api_object: ****************************************************")
						# 	print("format_api_object: ****************************************************")
						# 	#######################
						# else:
						# 	#######################
						# 	print("format_api_object: api_response.status_code: **FAIL**: ", api_response.status_code)
						# 	print("format_api_object: api_response.status_code: **FAIL**: ", api_response.status_code)
						# 	#######################
					#######################
					#######################
					#######################
					#######################
					end_date 	= api_object[a][b]["describe"]["end_date"] 
					start_date 	= api_object[a][b]["describe"]["start_date"] 
					#######################
					for c in api_object[a][b]:
						#######################
						if type(api_object[a][b][c]) is not str and str(c) is not "describe":
							for d in api_object[a][b][c]:
								if d == "url":
									api_object[a][b][c][d] = api_object[a][b][c][d].replace("similarweb_api_key", str(api_object["api_key"])).replace("user_end_date", str(end_date)).replace("user_start_date", str(start_date))
	return api_object

#####################################################################

def open_ids_csv(filename):
	read_file 	=  open(str(filename)+".csv","r", encoding="utf-8")
	csv_reader 	= csv.reader(read_file)
	return [a for a in csv_reader]
	
#####################################################################

# def get_categories(app_ids):
# 	categories = []
# 	for a in app_ids:
# 		if a not in categories:
# 			categories.append(a)
# 	return categories

#####################################################################

def create_category_folder(category):
	if not os.path.exists(str(category)):
		os.makedirs(category)

#####################################################################


def gplay_app_overview(app_id):
	#########################
	p 			= subprocess.Popen(["node", "gplay_app_overview.js", app_id], stdout=subprocess.PIPE)
	#########################
	out 		= p.stdout.read()
	#########################
	out 		= out.decode()
	out 		= re.sub( r'\n\s*(\S+)\s*:', r'\n"\1":', out )
	out 		= re.sub( r',\s*}', r'\n}', out )
	out 		= re.sub(r'<[^>]*>', '', out)
	out 		= json.dumps(out)
	out 		= json.loads(out)
	########################
	out 		= json.dumps(yaml.load(out))
	json_format = json.loads(out)
	########################
	# print("gplay_app_overview: json_format: ", json_format)
	########################
	return json_format


def gplay_permissions(app_id):
	#########################
	p 			= subprocess.Popen(["node", "gplay_permissions.js", app_id], stdout=subprocess.PIPE)
	#########################
	out 		= p.stdout.read()
	#########################
	out 		= out.decode()
	out 		= re.sub( r'\n\s*(\S+)\s*:', r'\n"\1":', out )
	out 		= re.sub( r',\s*}', r'\n}', out )
	out 		= re.sub(r'<[^>]*>', '', out)
	out 		= json.dumps(out)
	out 		= json.loads(out)
	########################
	out 		= json.dumps(yaml.load(out))
	json_format = json.loads(out)
	########################
	# print("gplay_permissions: json_format: ", json_format)
	########################
	return json_format


def gplay_developer(dev_id):
	#########################
	p 			= subprocess.Popen(["node", "gplay_dev.js", dev_id], stdout=subprocess.PIPE)
	#########################
	out 		= p.stdout.read()
	#########################
	out 		= out.decode()
	out 		= re.sub( r'\n\s*(\S+)\s*:', r'\n"\1":', out )
	out 		= re.sub( r',\s*}', r'\n}', out )
	out 		= re.sub(r'<[^>]*>', '', out)
	out 		= json.dumps(out)
	out 		= json.loads(out)
	########################
	out 		= json.dumps(yaml.load(out))
	json_format = json.loads(out)
	########################
	# print("gplay_developer: json_format: ", json_format)
	########################
	return json_format


def gplay_reviews(app_id, review_num, page_token):
	#########################
	print("gplay_reviews: review_num: ", review_num)
	#########################
	# per = "3000"
	#########################
	# p 			= subprocess.Popen(["node", "gplay_reviews.js", app_id, str(review_num)], stdout=subprocess.PIPE)
	p 			= subprocess.Popen(["node", "gplay_reviews.js", app_id, "3000", page_token], stdout=subprocess.PIPE)
	#########################
	out 		= p.stdout.read()
	#########################
	out 		= out.decode()
	out 		= re.sub( r'\n\s*(\S+)\s*:', r'\n"\1":', out )
	out 		= re.sub( r',\s*}', r'\n}', out )
	out 		= re.sub(r'<[^>]*>', '', out)
	out 		= json.dumps(out)
	out 		= json.loads(out)
	########################
	out 		= json.dumps(yaml.load(out))
	json_format = json.loads(out)
	########################
	# print("gplay_reviews: json_format: ", json_format)
	########################
	if json_format["nextPaginationToken"] is not page_token:
		time.sleep(0.1)
		gplay_reviews(app_id, review_num, json_format["nextPaginationToken"])
		# gplay_reviews(app_id, review_num, json_format["nextPaginationToken"], count_index+3000)
	########################
	return json_format


def gplay_data_safety(app_id):
	#########################
	p 			= subprocess.Popen(["node", "gplay_data_safety.js", app_id], stdout		=subprocess.PIPE)
	#########################
	out 		= p.stdout.read()
	out 		= str(out).replace(r"\n", "")
	out 		= out.replace('"', '')[1:]
	out 		= out.replace("'", "\"")
	########################
	# print("gplay_data_safety: out: ", out)
	########################
	out 		= json.dumps(yaml.load(out))
	json_format = json.loads(out)
	return json_format

# def gplay_single_init(app_id):


def gplay_all_init(app_ids):
	#######################
	print("gplay_all_init: ***************** START *****************")
	print("gplay_all_init: ***************** START *****************")
	print("gplay_all_init: ***************** START *****************")
	#######################
	current_month 	= str(datetime.now().month)
	if len(current_month) == 1:
		current_month = "0"+str(current_month)
	
	current_day 	= str(datetime.now().day)
	if len(current_day) == 1:
		current_day = "0"+str(current_day)
	
	current_year 	= str(datetime.now().year)
	#######################
	for z, a in enumerate(app_ids):
		#######################
		gplay_entry = {}
		#######################
		print("gplay_all_init: z: ", z)
		print("gplay_all_init: z: ", z)
		print("gplay_all_init: z: ", z)
		#######################
		save_path = str("sw_data/"+str(a[1]).lower()+"/"+a[0].replace(".", "")+"/google_play_data").replace(" ", "")
		save_filepath = str("sw_data/"+str(a[1]).lower()+"/"+a[0].replace(".", "")+"/google_play_data/"+str(a[0]).replace(".", "")+"_"+str(current_month+current_day+current_year)).replace(" ", "")
		create_category_folder(save_path)
		#######################
		# if z is not 0 and os.path.exists(save_filepath) == False:
		if os.path.exists(save_filepath) == False:
			app_id = a[0]
			if app_id == "com.att.callprotect":
				app_id = "com.att.mobilesecurity"
			
			
			print("gplay_all_init: a: ", str(a))
			print("gplay_all_init: app_id: ", str(app_id))
			app_overview 	= gplay_app_overview(app_id)
			print("gplay_all_init: app_overview: ", str(app_overview))
			gplay_entry["app_overview"] = app_overview
			
			dev_id = ""
			try:	
				dev_id 			= app_overview["developerId"]
			except:
				pass
			
			review_num = ""
			try:	
				review_num 		= app_overview["reviews"]
			except:
				pass
			# print("gplay_all_init: app_overview: ", app_overview)
			# print("gplay_all_init: dev_id: ", dev_id)
			# print("gplay_all_init: review_num: ", review_num)
			# print("#"*10)
			time.sleep(0.1)

			dev_info = ""
			try:
				dev_info 		= gplay_developer(dev_id)
			except:
				pass

			gplay_entry["dev_info"] = dev_info
			# print("gplay_all_init: dev_info: ", dev_info)
			# print("#"*10)
			time.sleep(0.1)
			
			data_safety = ""
			try:
				data_safety 	= gplay_data_safety(app_id)
			except:
				pass

			gplay_entry["data_safety"] = data_safety
			# print("gplay_all_init: data_safety: ", data_safety)
			# print("#"*10)
			time.sleep(0.2)

			perm = ""
			try:
				perm 			= gplay_permissions(app_id)
			except:
				pass

			gplay_entry["permissions"] = perm
			# print("gplay_all_init: perm: ", perm)
			# print("#"*10)
			time.sleep(0.1)

			# gplay_reviews(app_id, review_num, "first", 0)
			# rev 			= gplay_reviews(app_id, review_num, "first")
			# gplay_entry["reviews"] = rev
			# print("gplay_all_init: rev: ", rev)
			# print("#"*10)
			# time.sleep(0.1)

			# print("#"*10)
			# print("#"*10)
			# print("gplay_all_init: app_id: ", app_id)
		# print("gplay_all_init: gplay_entry: ", gplay_entry)
		print("#"*50)
		print("#"*50)

		# save_path = "sw_data/"+str(a[1]).lower()+"/"+a[0].replace(".", "")+"/google_play_data"
		# create_category_folder(save_path)


		if os.path.exists(save_filepath) == False:
			print("gplay_all_init: save_filepath: ", save_filepath)
			print("gplay_all_init: gplay_entry: ", gplay_entry)
			write_to_json(save_filepath, gplay_entry)

	print("gplay_all_init: ***************** END *****************")
	print("gplay_all_init: ***************** END *****************")
	print("gplay_all_init: ***************** END *****************")


#####################################################################

def write_to_json(filename, json_data):
	new_file = open(str(filename)+".json","w", encoding="utf-8")
	json.dump(json_data, new_file, indent=2)

def call_json_describe_endpoint(endpoint_url):
	print("call_json_describe_endpoint: endpoint_url: ", endpoint_url)
	add_key_url = endpoint_url.replace("similarweb_api_key", api_object["api_key"]) 
	print("call_json_describe_endpoint: add_key_url: ", add_key_url)
	return requests.get(add_key_url)

def call_json(endpoint_url):
	return requests.get(endpoint_url)

def format_json(json_data):
	call_get = json_data.content
	return  json.loads(call_get)

#####################################################################

# def call_api(app_ids):
# 	#######################
# 	for z, a in enumerate(app_ids):
# 		#######################
# 		print("call_api: ***************** START *****************")
# 		print("call_api: ***************** START *****************")
# 		print("call_api: ***************** START *****************")
# 		print("call_api: z: ", z)
# 		print("call_api: z: ", z)
# 		print("call_api: z: ", z)
# 		# if z is not 0:	
# 		# if z is not 0 and z >= 17 and a[0] != "com.linkedin.android" and a[0] != "com.intuit.quickbooks" and a[0] != "com.aadhk.woinvoice":
# 		# if z > 81 and a[0]:
# 		if a[0]:
# 			print("call_api: a: ", a)
# 			print("call_api: a[0]: ", a[0])
# 			#######################
# 			save_path = "sw_data/"+str(a[1]).lower()+"/"+a[0].replace(".", "")
# 			create_category_folder(save_path)
# 			#######################
# 			for b in api_object:
# 				#######################
# 				print("call_api: b: ", b)
# 				# print("call_api: api_object[b]: ", api_object[b])
# 				#######################
# 				if type(api_object[b]) is not str:
# 					for c in api_object[b]:
# 						print("call_api: c: ", c)
# 						#######################
# 						if type(api_object[b][c]) is not str and c != "describe" and c != "affinity":
# 							for d in api_object[b][c]:
# 								save_filepath = "sw_data/"+str(a[1]).lower()+"/"+a[0].replace(".", "")+"/"+str(a[0]).replace(".", "")+"_"+str(api_object[b][c]["describe"]["start_date"])+"_"+str(api_object[b][c]["describe"]["end_date"])+"_"+str(c)+"_"+str(d)
# 								if os.path.exists(save_filepath) == False and d != "describe":
# 									print("call_api: d: ", d)
# 									url_add_id = api_object[b][c][d]["url"].replace("app_id", str(a[0]))
# 									print("call_api: url_add_id: ", url_add_id)
# 									api_response 		= call_json(url_add_id)
# 									print("call_api: api_response: ", api_response)
# 									if api_response.status_code == 200:	
# 										formatted_response 	= format_json(api_response)
# 										print("call_api: formatted_response: ", formatted_response)
# 										write_to_json(save_filepath, formatted_response)
# 									# save_path
# 						#######################
# 					#######################
# 	print("call_api: ***************** END *****************")
# 	print("call_api: ***************** END *****************")
# 	print("call_api: ***************** END *****************")


def android_call_api(app_ids, api_object):
	#######################
	date_path_string = "sw_12_16_2023"
	#######################
	for z, a in enumerate(app_ids):
		#######################
		print("android_call_api: ***************** START *****************")
		print("android_call_api: ***************** START *****************")
		print("android_call_api: ***************** START *****************")
		print("android_call_api: z: ", z)
		print("android_call_api: z: ", z)
		print("android_call_api: z: ", z)
		if z is not 0:	
		# if z is not 0 and z >= 17 and a[0] != "com.linkedin.android" and a[0] != "com.intuit.quickbooks" and a[0] != "com.aadhk.woinvoice":
		# if z > 81 and a[0]:
		# if a[0] and z > 0:
		# if a[0] and z > 114:
		# if a[0] and z > 260:
			print("android_call_api: a: ", a)
			print("android_call_api: a[0]: ", a[0])
			#######################
			# save_path = "sw_7_29_2023/"+a[0].replace(".", "")
			save_path = date_path_string+"/"+a[0].replace(".", "")
			create_category_folder(save_path)
			#######################
			for b in api_object:
				#######################
				print("android_call_api: b: ", b)
				# print("android_call_api: api_object[b]: ", api_object[b])
				#######################
				if type(api_object[b]) is not str:
					for c in api_object[b]:
						print("android_call_api: c: ", c)
						#######################
						if type(api_object[b][c]) is not str and c != "describe" and c != "affinity":
							for d in api_object[b][c]:
								save_filepath = date_path_string+"/"+a[0].replace(".", "")+"/"+str(a[0]).replace(".", "")+"_"+str(api_object[b][c]["describe"]["start_date"])+"_"+str(api_object[b][c]["describe"]["end_date"])+"_"+str(c)+"_"+str(d)
								# save_filepath = "sw_data/"+str(a[10]).lower()+"/"+a[0].replace(".", "")+"/"+str(a[0]).replace(".", "")+"_"+str(api_object[b][c]["describe"]["start_date"])+"_"+str(api_object[b][c]["describe"]["end_date"])+"_"+str(c)+"_"+str(d)
								if os.path.exists(save_filepath) == False and d != "describe":
									print("android_call_api: d: ", d)
									url_add_id = api_object[b][c][d]["url"].replace("app_id", str(a[0]))
									print("android_call_api: url_add_id: ", url_add_id)
									api_response 		= call_json(url_add_id)
									print("android_call_api: api_response: ", api_response)
									if api_response.status_code == 200:	
										formatted_response 	= format_json(api_response)
										print("android_call_api: formatted_response: ", formatted_response)
										write_to_json(save_filepath, formatted_response)
									# save_path
						#######################
					#######################
	print("android_call_api: ***************** END *****************")
	print("android_call_api: ***************** END *****************")
	print("android_call_api: ***************** END *****************")


def apple_call_api(app_ids, api_object):
	#######################
	for z, a in enumerate(app_ids):
		#######################
		print("call_api: ***************** START *****************")
		print("call_api: ***************** START *****************")
		print("call_api: ***************** START *****************")
		print("call_api: z: ", z)
		print("call_api: z: ", z)
		print("call_api: z: ", z)
		# if z is not 0:	
		# if z is not 0 and z >= 17 and a[0] != "com.linkedin.android" and a[0] != "com.intuit.quickbooks" and a[0] != "com.aadhk.woinvoice":
		# if z > 81 and a[0]:
		if a[1] and z > 0:
			print("call_api: a: ", a)
			print("call_api: a[0]: ", a[1])
			#######################
			save_path = "sw_data/"+str(a[10]).lower()+"/"+a[1].replace(".", "")
			create_category_folder(save_path)
			#######################
			for b in api_object:
				#######################
				print("call_api: b: ", b)
				# print("call_api: api_object[b]: ", api_object[b])
				#######################
				if type(api_object[b]) is not str:
					for c in api_object[b]:
						print("call_api: c: ", c)
						#######################
						if type(api_object[b][c]) is not str and c != "describe" and c != "affinity":
							for d in api_object[b][c]:
								save_filepath = "sw_data/"+str(a[10]).lower()+"/"+a[1].replace(".", "")+"/"+str(a[0]).replace(".", "")+"_"+str(api_object[b][c]["describe"]["start_date"])+"_"+str(api_object[b][c]["describe"]["end_date"])+"_"+str(c)+"_"+str(d)
								if os.path.exists(save_filepath) == False and d != "describe":
									print("call_api: d: ", d)
									url_add_id = api_object[b][c][d]["url"].replace("app_id", str(a[1]))
									print("call_api: url_add_id: ", url_add_id)
									api_response 		= call_json(url_add_id)
									print("call_api: api_response: ", api_response)
									if api_response.status_code == 200:	
										formatted_response 	= format_json(api_response)
										print("call_api: formatted_response: ", formatted_response)
										write_to_json(save_filepath, formatted_response)
									# save_path
						#######################
					#######################
	print("call_api: ***************** END *****************")
	print("call_api: ***************** END *****************")
	print("call_api: ***************** END *****************")

#####################################################################

# def get_daily_active_users(app_id, start_date, end_date):
# 	#######################
# 	# EX: app_id = "com.tabtrader.android", start_date = "2022-12", end_date = "2022-10"
# 	#######################
# 	url 				= "https://api.similarweb.com/v1/app/Google/"+app_id+"/engagement/dau?api_key="+api_object.api_key+"&start_date="+start_date+"&end_date="+end_date+"&country=us&granularity=monthly&format=json"
# 	api_response 		= call_json(url)
# 	formatted_response 	= format_json(api_response)
# 	#######################
# 	print(url)
# 	print("*"*50)
# 	print(api_response)
# 	print("*"*50)
# 	print(formatted_response)
# 	print("*"*50)
# 	#######################
# 	write_to_json(str(app_id)+"_dau_"+str(start_date)+"_"+str(end_date), formatted_response)
	#######################

def init():
	global android_api_object
	global apple_api_object
	#######################
	android_api_object 	= format_api_object_describe_endpoint(android_api_object)
	# android_app_ids 	= open_ids_csv("review_list")
	android_app_ids 	= open_ids_csv("download_list")
	android_call_api(android_app_ids, android_api_object)
	#######################
	# apple_api_object 	= format_api_object_describe_endpoint(apple_api_object)
	# apple_app_ids 		= open_ids_csv("review_list")
	# apple_app_ids 	= [["com.hunter.vegas.casino.game","1661499348","Cash Hunter Slots-Casino Game","Glacier Game","","","","0","79","F","Game/Casino","1/4/2022"], ["com.gk.themeparkfun3d","1594613604","Theme Park 3D - Fun Aquapark","Alictus","","","","24","78","F","Game/Simulation","1/4/2022"]]
	# apple_call_api(apple_app_ids, apple_api_object)
	#######################
	# app_ids 	= [["com.linkedin.android","Business"], ["com.linkedin.android","Business"]]
	# print(app_ids)
	# app_ids = [app_ids[0], app_ids[0]]
	#######################
	#######################
	# gplay_all_init(app_ids)
	#######################


init()