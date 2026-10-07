#####################################################################
import os, requests, json, csv, subprocess, yaml, re, time
from datetime import datetime
from dateutil.relativedelta import relativedelta
#####################################################################


def read_csv(filename):
	read_file 	=  open(str(filename)+".csv","r", encoding="utf-8", errors="ignore")
	csv_reader 	= csv.reader((line.replace('\0','') for line in read_file))
	csv_rows 	= [a for a in csv_reader]
	read_file.close()
	return csv_rows


def open_ids_csv(filename):
	read_file 	=  open(str(filename)+".csv","r", encoding="utf-8", errors="ignore")
	csv_reader 	= csv.reader(read_file)
	return [a[0] for a in csv_reader]


def gplay_app_overview(app_id):
	#########################
	p 			= subprocess.Popen(["node", "gplay_app_overview.js", app_id], stdout=subprocess.PIPE)
	# print(p)
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
	# out 		= json.dumps(yaml.load(out))
	out 		= json.dumps(yaml.safe_load(out))
	json_format = json.loads(out)
	########################
	# print("gplay_app_overview: json_format: ", json_format)
	########################
	return json_format


def write_object_to_csv(reviews_array, filename):
    # Get all unique criteria values
	for obj in reviews_array:	
		criteria_values = set()
		for criteria in obj.get('criterias', []):
			criteria_values.add(criteria['criteria'])

		# Create a list of fieldnames for CSV header
		fieldnames = list(obj.keys()) + list(criteria_values)

		# Write object to CSV file
		with open(filename, 'a', newline='', encoding='utf-8', errors='ignore') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			if csvfile.tell() == 0:
				writer.writeheader()
			writer.writerow({**obj, **{criteria: next((c['rating'] for c in obj['criterias'] if c['criteria'] == criteria), None) for criteria in criteria_values}})


def gplay_reviews(app_id, review_num, page_token):
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
	# out 		= json.dumps(yaml.load(out))
	out 		= json.dumps(yaml.safe_load(out))
	json_format = json.loads(out)
	########################
	# asdf = get_unique_keys(json_format)
	# asdf = get_keys(json_format["data"])
	write_object_to_csv(json_format["data"], "123.csv")
	# print("gplay_reviews: json_format: ", json_format)
	# print("gplay_reviews: asdf: ", asdf)
	########################
	if json_format["nextPaginationToken"] is not page_token:
		time.sleep(0.1)
		gplay_reviews(app_id, review_num, json_format["nextPaginationToken"])
	########################
	return json_format


def init_gplay(app_id_list):
	for a, b in enumerate(app_id_list):
		# if a > 0 and a < 3:
		if a > 0:
			print("index: ", a)
			print("app_id: ", b)
			app_json 	= gplay_app_overview(b)
			num_reviews = app_json["reviews"]
			print("num_reviews: ", num_reviews)
			gplay_reviews(b, num_reviews, "")
			print("*"*50)


def init():
	# asdf = read_csv("123")
	# print(asdf)
	filename 	= "appid_review_0703"
	app_id_list = open_ids_csv(filename)
	init_gplay(app_id_list)

init()





















































##########################################################
# vvv SCRATCH vvv
##########################################################



# def get_keys(rev_obj):
# 	# print(rev_obj)
# 	a = []
# 	for b in rev_obj:
# 		for c in b:
# 			# print(c)
# 			if c not in a:
# 				a.append(c)
# 			if "criterias" in c:
# 				for d in b[c]:
# 					if d["criteria"] not in a:
# 						print(d["criteria"])
# 						a.append(d["criteria"])
# 	print(a)
# 	print(len(a))

# def get_unique_keys(obj_array):
#     keys = set()
#     for obj in obj_array:
#         for key in obj:
#             keys.add(key)
#             if isinstance(obj[key], dict):
#                 nested_keys = get_unique_keys([obj[key]])
#                 keys.update(nested_keys)
#     return list(keys)