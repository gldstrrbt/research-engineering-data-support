#####################################################################
# import os, requests, json, csv, subprocess, yaml, re, time
import os, requests, json, csv, subprocess, re, time
from datetime import datetime
from dateutil.relativedelta import relativedelta
#####################################################################
from ruamel.yaml import YAML
from ruamel.yaml.reader import Reader
#####################################################################


def read_csv(filename):
	read_file 	=  open(str(filename),"r", encoding="utf-8", errors="ignore")
	csv_reader 	= csv.reader((line.replace('\0','') for line in read_file))
	csv_rows 	= [a for a in csv_reader]
	read_file.close()
	return csv_rows


# vvv RETURNS ONLY THE IDS FROM ROWS OF A CSV vvv #
def open_ids_csv(filename):
	read_file 	=  open(str(filename)+".csv","r", encoding="utf-8", errors="ignore")
	csv_reader 	= csv.reader(read_file)
	return [a[0] for a in csv_reader]


# vvv RETURNS FULL ROWS OF A CSV vvv #
def open_csv(filename):
	read_file 	=  open(str(filename)+".csv","r", encoding="utf-8", errors="ignore")
	csv_reader 	= csv.reader(read_file)
	return [a for a in csv_reader]


def write_csv(new_filename, data):
	csvfile = open(filename+".csv", 'w', newline='', encoding='utf-8', errors='ignore')
	writer 	= csvfile.writer(csvfile)
	csv.writerows(data)


def strip_invalid(s):
    res = ''
    for x in s:
        if Reader.NON_PRINTABLE.match(x):
            # res += '\\x{:x}'.format(ord(x))
            continue
        res += x
    return res


def gplay_app_overview(app_id):
	#########################
	yaml 		= YAML(typ='safe')
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
	# out 		= json.dumps(yaml.safe_load(out))
	out 		= json.dumps(yaml.load(strip_invalid(out)))
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


def gplay_reviews(app_id, review_num, page_token, row_is_dupe):
	#########################
	yaml 		= YAML(typ='safe')
	#########################
	# per = "3000"
	#########################
	# p 			= subprocess.Popen(["node", "gplay_reviews.js", app_id, str(review_num)], stdout=subprocess.PIPE)
	# p 			= subprocess.Popen(["node", "gplay_reviews.js", app_id, "3000", page_token], stdout=subprocess.PIPE)
	# if page_token == None:
	# 	page_token = ""
	print(app_id, review_num, page_token)
	print(app_id, review_num, page_token)
	print(app_id, review_num, page_token)
	if page_token != None:
		# page_token = ""
		# try:
		p 			= subprocess.Popen(["node", "gplay_reviews.js", app_id, str(review_num), page_token], stdout=subprocess.PIPE)
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
		try:	
			out 		= json.dumps(yaml.load(strip_invalid(out)))
			json_format = json.loads(out)
			########################
			existing_rows   = []
			filename        = app_id.replace(".", "_")
			file_path       =  "./0_reviews/"+str(filename)+".csv"
			if os.path.exists(file_path) and row_is_dupe == True:
				try:
					existing_rows = read_csv(file_path)
				except IOError:
					print(f"An error occurred while creating the file '{file_path}'.")
			# else:
			#     print(f"File '{file_path}' already exists.")
			########################
			# asdf = get_unique_keys(json_format)
			# asdf = get_keys(json_format["data"])
			if json_format["data"][0] not in existing_rows:
				print("json_format[data][0]: ", json_format["data"][0])
				write_object_to_csv(json_format["data"], file_path)
				row_is_dupe = False
			# print("gplay_reviews: json_format: ", json_format)
			# print("gplay_reviews: asdf: ", asdf)
			########################
			if json_format["nextPaginationToken"] is not page_token:
				time.sleep(0.1)
				gplay_reviews(app_id, review_num, json_format["nextPaginationToken"], row_is_dupe)
			########################
			return json_format
		except:
			pass


def init_gplay(app_id_list):
	for a, b in enumerate(app_id_list):
		# if a > 0 and a < 3:
		# if a > 0:
		print(a)
		# if a > 3:
		# if a > 0 and b not in ['com.azarlive.android', 'me.talkyou.app.im', 'com.textra', 'com.zhiliaoapp.musically', 'com.yahoo.mobile.client.android.fantasyfootball']:
		# if a > 22 and b not in ['com.azarlive.android', 'me.talkyou.app.im', 'com.textra', 'com.zhiliaoapp.musically', 'com.yahoo.mobile.client.android.fantasyfootball']:
		if a > 0 and b not in ['com.azarlive.android', 'me.talkyou.app.im', 'com.textra', 'com.zhiliaoapp.musically', 'com.yahoo.mobile.client.android.fantasyfootball']:
			print("index: ", a)
			print("app_id: ", b)
			# if b != None and b != "app_id":
			filename = b.replace(".", "_")
			file_path = "./0_reviews/"+str(filename)+".csv"
			# if b != None and b != "app_id" and b != "com.linkedin.android" and b != "com.att.mobilesecurity" and os.path.exists(file_path) == False:
				
			app_id = b
			if app_id == "com.att.callprotect":
				app_id = "com.att.mobilesecurity"

			elif app_id == "jp.pxv.android":
				app_id = "jp.pxv.android.manga"

			app_json 	= gplay_app_overview(app_id)
			if app_json:
				num_reviews = app_json["reviews"]
				print("num_reviews: ", num_reviews)
			
				gplay_reviews(app_id, num_reviews, "", True)
				print("*"*50)


def scan_dupes(app_id_list):
	new_id_list 	= []
	new_csv_array 	= []
	for a, b in enumerate(app_id_list):
		# if a > 0:
		if b[0] not in new_id_list:
			new_id_list.append(b[0])
			new_csv_array.append(b)
	return [new_id_list, new_csv_array]


def scan_not_downloaded(app_id_list, download_dir):
	not_downloaded 	= []
	download_list 	= [a.replace(".csv", "").replace("_", ".") for a in os.listdir(download_dir)]
	# print(download_list)
	for a, b in enumerate(app_id_list):
		if a > 0:
			if b not in download_list:
				not_downloaded.append(b)
	return not_downloaded


def init():
	########################
	app_id_filename 	= "list_review_download_rest_100323"
	app_id_list         = open_ids_csv(app_id_filename)
	# app_id_list         = ['com.azarlive.android', 'me.talkyou.app.im', 'com.textra', 'com.zhiliaoapp.musically', 'com.yahoo.mobile.client.android.fantasyfootball']
	print(app_id_list[0])
	print(app_id_list[0])
	print(app_id_list[0])
	print(app_id_list[0])
	print(app_id_list[0])
	print(app_id_list[0])
	########################
	init_gplay(app_id_list)
	########################
	# app_id_filename 	= "appid_review_0703"
	# app_id_list         = open_csv(app_id_filename)
	# dupes_removed 		= scan_dupes(app_id_list)
	# new_filename 		= "appid_review_0703_no_dupes"
	# print(dupes_removed[1][0])
	# print(len(dupes_removed[0]))
	# download_dir 		= "./0_reviews" 
	# not_downloaded_ids = scan_not_downloaded(dupes_removed[0], download_dir)
	# print(not_downloaded_ids)
	# print(len(not_downloaded_ids))
	# write_csv(new_filename, dupes_removed)
	########################


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