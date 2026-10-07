#####################################################################
import os, requests, json, csv, subprocess, yaml
from datetime import datetime
from dateutil.relativedelta import relativedelta
#####################################################################

api_object = {
	"api_key": "REDACTED_API_KEY",
	"app_analysis_premium": {
		"engagement":{
			"describe":{
				"url":"https://api.similarweb.com/v4/data-ai/engagement/describe?api_key=REDACTED_API_KEY",
				"region":"US",
				"granularity": "Monthly",
				"start_date": "2021-10",
		        "end_date": "2022-12",
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
				"start_date": "2020-10",
		        "end_date": "2022-11",
		        "period":24
			},
			"day_30_retention":{
				"url": "https://api.similarweb.com/v4/data-ai/Google/app_id/retention-d30?api_key=REDACTED_API_KEY&start_date=user_start_date&end_date=user_end_date&country=us&granularity=monthly&device=androidPhone&format=json"
			}
		},
		"affinity":{
			"describe":{
				"url":"https://api.similarweb.com/v4/data-ai/audience-interests/describe?api_key=REDACTED_API_KEY",
				"region":"US",
				"granularity": "Monthly",
				"start_date": "2021-10",
		        "end_date": "2022-12",
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
				"start_date": "2021-10",
		        "end_date": "2022-12",
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
				"start_date": "2021-10",
		        "end_date": "2022-12",
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


def format_api_object_describe_endpoint():
	for a in api_object:
		if type(api_object[a]) is not str:
			for b in api_object[a]:
				if type(api_object[a][b]) is not str:
					#######################

					api_object[a][b]["describe"]["url"] = api_object[a][b]["describe"]["url"].replace("similarweb_api_key", str(api_object["api_key"]))
					api_response 						= call_json(api_object[a][b]["describe"]["url"])

					if api_response.status_code == 200:	
						#######################
						print("format_api_object: api_response.status_code: !!SUCCESS!!: ", api_response.status_code)
						print("format_api_object: api_response.status_code: !!SUCCESS!!: ", api_response.status_code)
						#######################
						# print("format_api_object: api_response: ", api_response)
						#######################
						formatted_response 	= format_json(api_response)
						# print("format_api_object: formatted_response: ", formatted_response)
						#######################
						print("format_api_object: api_object[a][b]: before: ", api_object[a][b])
						format_api_object_dates(api_object[a][b], formatted_response)
						print("format_api_object: api_object[a][b]: after: ", api_object[a][b])
						print("format_api_object: ****************************************************")
						print("format_api_object: ****************************************************")
						#######################
					else:
						#######################
						print("format_api_object: api_response.status_code: **FAIL**: ", api_response.status_code)
						print("format_api_object: api_response.status_code: **FAIL**: ", api_response.status_code)
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
	print(api_object)

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

# def gplay_single_init(app_id):

def gplay_all_init(app_ids):
	for z, a in enumerate(app_ids):
		#######################
		print("gplay_all_init: ***************** START *****************")
		print("gplay_all_init: ***************** START *****************")
		print("gplay_all_init: ***************** START *****************")
		print("gplay_all_init: z: ", z)
		print("gplay_all_init: z: ", z)
		print("gplay_all_init: z: ", z)
		if z is not 0:	
			print("gplay_all_init: a: ", a)
			# print("gplay_all_init: a[0]: ", a[0])

def gplay_data_safety(app_id):
	p = subprocess.Popen(["node", "index.js", "com.tabtrader.android"], stdout=subprocess.PIPE)
	#########################
	# p = subprocess.Popen(['node', 'index.js'], stdout=subprocess.PIPE)
	#########################
	out = p.stdout.read()
	out = str(out).replace(r"\n", "")
	out = out.replace('"', '')[1:]
	out = out.replace("'", "\"")
	########################
	print(out)
	########################
	out = json.dumps(yaml.load(out))
	json_format = json.loads(out)
	for a in json_format:
		print(a)

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

def call_api(app_ids):
	#######################
	for z, a in enumerate(app_ids):
		#######################
		print("call_api: ***************** START *****************")
		print("call_api: ***************** START *****************")
		print("call_api: ***************** START *****************")
		print("call_api: z: ", z)
		print("call_api: z: ", z)
		print("call_api: z: ", z)
		if z is not 0:	
			print("call_api: a: ", a)
			print("call_api: a[0]: ", a[0])
			#######################
			save_path = "sw_data/"+str(a[1]).lower()+"/"+a[0].replace(".", "")
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
						if type(api_object[b][c]) is not str and c != "describe":
							for d in api_object[b][c]:
								save_filepath = "sw_data/"+str(a[1]).lower()+"/"+a[0].replace(".", "")+"/"+str(a[0]).replace(".", "")+"_"+str(api_object[b][c]["describe"]["start_date"])+"_"+str(api_object[b][c]["describe"]["end_date"])+"_"+str(c)+"_"+str(d)
								if os.path.exists(save_filepath) == False and d != "describe":
									print("call_api: d: ", d)
									url_add_id = api_object[b][c][d]["url"].replace("app_id", str(a[0]))
									print("call_api: url_add_id: ", url_add_id)
									api_response 		= call_json(url_add_id)
									formatted_response 	= format_json(api_response)
									write_to_json(save_filepath, formatted_response)
									# save_path
						#######################
					#######################
	print("call_api: ***********************")

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
	#######################
	# format_api_object_periods()
	# app_ids 	= open_ids_csv("app_ids")
	#######################
	# print("app_ids", app_ids)
	#######################
	#######################
	format_api_object_describe_endpoint()
	app_ids 	= open_ids_csv("app_ids")
	#######################
	# print("init: app_ids", app_ids)
	#######################
	call_api(app_ids)
	#######################
	# get_daily_active_users("com.tabtrader.android", "2022-10", "2022-12")
	# get_daily_active_users("com.tabtrader.android", "2022-12", "2022-12")
	#######################


init()