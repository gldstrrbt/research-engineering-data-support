import os, requests, time, pyautogui, random, pickle, csv
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service



# options = Options()
# options.add_argument("--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--no-sandbox")
# options.add_argument("--start-maximized")
# options.add_argument("--disable-infobars")
# options.add_argument("--remote-debugging-port=9222")

# driver 	= webdriver.Firefox(executable_path=r"./geckodriver.exe", capabilities={"ignoreZoomSetting":True})


# profile = FirefoxProfile()
# profile.set_preference("browser.download.panel.shown", False)
# profile.set_preference("browser.helperApps.neverAsk.openFile","text/csv,application/vnd.ms-excel")
# profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword, application/csv, application/ris, text/csv, image/png, application/pdf, text/html, text/plain, application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream");
# profile.set_preference("browser.download.manager.showWhenStarting", False);
# profile.set_preference("browser.download.manager.alertOnEXEOpen", False);
# profile.set_preference("browser.download.manager.focusWhenStarting", False);
# profile.set_preference("browser.download.folderList", 2);
# profile.set_preference("browser.download.useDownloadDir", True);
# profile.set_preference("browser.helperApps.alwaysAsk.force", False);
# profile.set_preference("browser.download.manager.alertOnEXEOpen", False);
# profile.set_preference("browser.download.manager.closeWhenDone", True);
# profile.set_preference("browser.download.manager.showAlertOnComplete", False);
# profile.set_preference("browser.download.manager.useWindow", False);
# profile.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False);
# profile.set_preference("pdfjs.disabled", True);
# profile.set_preference("pdfjs.enabledCache.state", False);
# profile.set_preference("browser.download.dir", "E:\\Data\\_similarweb\\0_sw\\_selenium_data")
# driver 	= webdriver.Firefox(executable_path=r"./geckodriver.exe", options=options, firefox_profile=profile)

options = Options()
options.add_experimental_option("prefs", { "download.default_directory": r"E:\Data\_similarweb\0_sw\0_selenium_app_data"})
# driver 	= webdriver.Chrome(executable_path=r"./chromedriver.exe", options=options)



driver 	= webdriver.Chrome(service = Service("./chromedriver.exe"), options=options)


# profile.set_preference("browser.download.dir", "C:\\Users\\***\\****\\Desktop\\Automation")
# driver 	= webdriver.Firefox(executable_path=r"./geckodriver.exe", options=options)


# service = Service('./geckodriver.exe')
# driver = webdriver.Firefox(service=service)


# fp 		= webdriver.FirefoxProfile("./mso5hm58.default-release")


driver.set_window_position(800, -1000)
driver.set_window_size(850, 600)

# C:<local-user-path>/AppData/Roaming/Mozilla/Firefox/Profiles/mso5hm58.default-release


actions = ActionChains(driver) 



username = os.getenv("SIMILARWEB_USERNAME", "")
# password = "<redacted>"
# password = "<redacted>"
password = os.getenv("SIMILARWEB_PASSWORD", "")
# password = "<redacted>"
# password = "<redacted>"
# password = "<redacted>"
# password = "<redacted>"
# password = "<redacted>"
# password = "<redacted>"


# driver.get("https://www.amazon.com/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&switch_account=")
# driver.find_element_by_css_selector("#ap_email").send_keys("<redacted-email>")
# driver.find_element_by_css_selector("#ap_email").send_keys(Keys.RETURN)
# time.sleep(1)
# driver.find_element_by_css_selector("#ap_password").send_keys("<redacted-password>")
# driver.find_element_by_css_selector("#ap_password").send_keys(Keys.RETURN)
# time.sleep(1)
# driver.get("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")
# driver.find_element_by_css_selector(".a-button-input").click()
# time.sleep(1)
# driver.find_element_by_css_selector("a.a-button-text.a-text-center").click()
# time.sleep(1)
# driver.find_element_by_css_selector("input[type='submit'].a-button-text").click()

# states={
# 	"united states" :"840",
# 	"arizona" :"8404",
# 	"california" :"8406",
# 	"florida" :"84012",
# 	"georgia" :"84031",
# 	"illinois" :"84017",
# 	"massachusetts" :"84025",
# 	"michigan" :"84026",
# 	"new jersey" :"84034",
# 	"new york" :"84036",
# 	"north carolina" :"84037",
# 	"ohio" :"84039",
# 	"pennsylvania" :"84042",
# 	"texas" :"84048",
# 	"virginia" :"84051",
# 	"washington" :"84053"
# }

states={
	"united states" :"840",
	"california" :"8406",
	"new york" :"84036",
	"virginia" :"84051"
}

sources = ["all traffic", "desktop", "mobile web"]

duration_checked = False

def save_cookies():
	pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

def load_cookies():
	cookies = pickle.load(open("cookies.pkl", "rb"))
	for cookie in cookies:
		driver.add_cookie(cookie)

def zoom_out():
	pyautogui.keyDown("ctrl")
	pyautogui.press("-")
	pyautogui.keyUp("ctrl")

# def wait_for_download():
	# data-automation="Download Excel"
		# data-automation-button-loading="false"
			# data-automation-icon-name="excel"

def click_element(selector):
	print("auto_sw: click_element: selector: ", selector)
	# driver.find_element_by_css_selector(selector).click()
	driver.find_element(By.CSS_SELECTOR, selector).click()
	time.sleep(2)

def key_entry(key_value):
	actions = ActionChains(driver) 
	actions.send_keys(key_value)
	actions.perform()

def type_input(string_value):
	for character in string_value:
		key_speed = random.uniform(1/6.8, 1/8.0)
		if character == "." or character == "@" or character.isdigit():
			key_speed = random.uniform(1/5.04, 1/6.5)
		print("auto_sw: login: key_speed: ", key_speed)
		print("auto_sw: login: character: ", character)
		key_entry(character)
		time.sleep(key_speed)

def login():
	###################################
	# print("auto_sw: login: test.value_of_css_property(display): ", test.value_of_css_property("display"))
	###################################
	click_element("#input-email")
	type_input(username)
	key_entry(Keys.TAB)
	type_input(password)
	key_entry(Keys.ENTER)
	###################################
	# type_input("#input-email", username)
	# key_entry(Keys.TAB)
	# type_input("#input-password", password)
	# key_entry(Keys.ENTER)
	###################################
	# type_input("#input-password", password)
	# driver.find_element_by_css_selector("").send_keys(password)
	# driver.find_element_by_css_selector('[data-automation-name="submit-button"]').click()
	# data-automation-name="submit-button"

# def download():
# 	data-automation-icon-name="excel"


def get_page(url):
	# a = requests.get(url)
	# b = a.text
	# a = driver.page_source
	driver.get(url)
	time.sleep(1)
	a = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
	return a

def click_country_dropdown(new_state):
	print("auto_sw: click_country_dropdown: new_state: ", new_state)
	driver.find_element_by_css_selector(".DropdownButton--filtersBarDropdownButton--country").click()
	time.sleep(1)
	click_element(".DropdownContent-search")
	time.sleep(1)
	type_input(new_state)
	time.sleep(1)
	dropdown_items 		= driver.find_elements_by_css_selector('[data-automation="country-text"]')
	print("auto_sw: click_country_dropdown: dropdown_items: ", dropdown_items)
	for a in dropdown_items:
		try:
			if a.text.lower() == new_state.lower():
				a.click()
				print("auto_sw: click_country_dropdown: a: ", a)
		except:
			print("!!! auto_sw: click_country_dropdown: a: failed !!!")
			pass
		# CountryFilter-dropdownButton
	# driver.find_element_by_css_selector(".CountryDropdownItem")

def click_websource_dropdown(websource):
	country_dropdown 	= driver.find_element_by_css_selector(".WebSourceFilter-dropdownButton").click()
	time.sleep(1)
	dropdown_items 		= driver.find_elements_by_css_selector(".WebSourceDropdownItem")
	for a in dropdown_items:
		try:
			if a.text.lower() == websource.lower():
				a.click()
				print("auto_sw: click_websource_dropdown: a: ", a)
		except:
			print("!!! auto_sw: click_websource_dropdown: a: failed !!!")
			pass



def wait_main_page():
	main_loaded = False
	while main_loaded == False:
		# greeting_text = driver.find_elements_by_css_selector("div")
		greeting_text = driver.find_elements(By.CSS_SELECTOR, "div")
		for div in greeting_text:
			try:
				if div.text == "Hi Shane" or "Hi, Welcome to Similarweb" in div.text:
					main_loaded = True
					print("auto_sw: wait_main_page: div.text: ", div.text)
					time.sleep(1)
			except:
				pass

def wait_website(website_url):
	main_loaded = False
	while main_loaded == False:
		# greeting_text = driver.find_elements_by_css_selector(".wwo-widgets span")
		greeting_text = driver.find_elements(By.CSS_SELECTOR, ".wwo-widgets span")
		for div in greeting_text:
			time.sleep(2)
			try:
				if str(website_url) in div.text:
					main_loaded = True
					print("auto_sw: wait_website: div.text: ", div.text)
					print("auto_sw: wait_website: div.text: fuckkkkkkkkkk")
					return
					# time.sleep(1)
			except:
				pass

# def main_page_input():
# 	input-container

# profile = "<local-user-path>\AppData\Local\Temp\rust_mozprofiley2yzQR"

def cycle_websource(timewait):
	for z in sources:
		time.sleep(timewait)
		click_websource_dropdown(z)
	

def cycle_menu(active_state):
	global duration_checked
	# 1 download for channel traffic = 5 seconds after clicking
	click_element('[data-automation-item="analysis.traffic.engagement.title"]')
	
	if duration_checked == False:	
		time.sleep(3)
		duration_select()
		time.sleep(1)
		click_apply()
		duration_checked = True

	if active_state == "united states":
		cycle_websource(3)
	time.sleep(3)
	
	# 1 download for channel traffic = 2 seconds after clicking
	# 1 download for traffic sources = 15 seconds after clicking
	click_element('[data-automation-item="analysis.traffic.marketing.channels.title"]')
	if active_state == "united states":
		cycle_websource(3)
	time.sleep(3)

	# 1 download for audience interests = 25-30 seconds after clicking
	# LONG TIME TO LOAD PAGE
	click_element('[data-automation-item="analysis.audience.interests.title"]')
	if active_state == "united states":
		cycle_websource(10)
	time.sleep(10)

def duration_select():
	duration_dropdown = driver.find_elements_by_css_selector(".DropdownButton--filtersBarDropdownButton")
	for a in duration_dropdown:
		if "months" in a.text.lower() and "12 months" not in a.text.lower():
			a.click()
			time.sleep(2)
			month_buttons = driver.find_elements_by_css_selector("#calendar-presets-container div div")
			for b in month_buttons:
				if "last 12 months" in b.text.lower():
					print("auto_sw: duration_select: b.text.lower(): ", b.text.lower())
					b.click()


def click_apply():
	time.sleep(1)
	try:
		apply_button = driver.find_element_by_css_selector(".DurationSelector-container .DurationSelector-action-submit")
		apply_button.click()
	except:
		pass


def check_sites(site_list):
	###################################
	for a, b in enumerate(site_list):
		###################################
		if a == 0:
			###################################
			click_element(".input-container")
			type_input(b)
			time.sleep(1)
			click_element(".ListItemWebsite")
			###################################
		else:
			###################################
			# .AutocompleteWebsitesQueryBar
			###################################
			try:
				click_element('[data-automation="query-bar-item-text"]')
			except:
				pass			
			###################################
			try:
				click_element('[data-automation="query-bar-item-text"]')
			except:
				pass
			###################################
			type_input(b)
			time.sleep(1)
			key_entry(Keys.ENTER)
			key_entry(Keys.ENTER)
			time.sleep(1)
			click_element('[data-automation-item="analysis.overview.performance.title"]')
			###################################
		###################################
		time.sleep(2)
		wait_website(b)
		print("auto_sw: wait_website: PASSED")
		# time.sleep(1)
		###################################
		for x in states:
			###################################
			print("auto_sw: check_sites: x: ", x)
			###################################
			time.sleep(3)
			click_country_dropdown(x)
			time.sleep(3)
			###################################
			cycle_menu(x)
			###################################


		# 1 download for demographics = 2 seconds after clicking
		# NO STATES
		# for z in sources:
		click_element('[data-automation-item="analysis.audience.demo.title"]')
		time.sleep(3)
		cycle_websource(3)
		time.sleep(3)
		time.sleep(3)



def init_manual():
	###################################
	login_url = "https://pro.similarweb.com/"
	get_page(login_url)
	###################################
	zoom_out()
	zoom_out()
	zoom_out()
	###################################
	# if os.path.exists("cookies.pkl") == True:
	# 	load_cookies()
	###################################
	login()
	###################################
	wait_main_page()
	###################################
	time.sleep(1)
	zoom_out()
	time.sleep(0.15)
	zoom_out()
	time.sleep(0.15)
	zoom_out()
	time.sleep(1)
	###################################
	# site_list = ["linkedin.com", "google.com", "facebook.com", "amazon.com"]
	# site_list = ["google.com", "youtube.com", "pornhub.com", "facebook.com", "reddit.com", "amazon.com", "twitter.com", "xvideos.com", "yahoo.com", "wikipedia.org", "weather.com", "fandom.com", "instagram.com", "duckduckgo.com", "walmart.com", "xnxx.com", "bing.com", "tiktok.com", "xhamster.com", "ebay.com", "cnn.com", "onlyfans.com", "taboola.com", "usps.com", "twitch.tv", "quora.com", "foxnews.com", "espn.com", "chaturbate.com", "nytimes.com", "tremendous.com", "imdb.com", "microsoftonline.com", "paypal.com", "live.com", "etsy.com", "linkedin.com", "dood.re", "netflix.com", "office.com", "simpcity.su", "accuweather.com", "ups.com", "microsoft.com", "discord.com", "msn.com", "pinterest.com", "dailymail.co.uk", "blogspot.com", "apple.com", "indeed.com", "bestbuy.com", "fedex.com", "zoom.us", "tumblr.com", "target.com", "stripchat.com", "xhamster18.desi", "ign.com", "nypost.com", "patreon.com", "zillow.com", "gamespot.com", "spotify.com", "samsung.com", "livejasmin.com", "homedepot.com", "roblox.com", "erome.com", "eporner.com", "capitalone.com", "github.com", "marca.com", "craigslist.org", "hulu.com", "instructure.com", "steamcommunity.com", "xfinity.com", "bbc.com", "chase.com", "www1.gogoanime.ar", "youporn.com", "t-mobile.com", "usatoday.com", "wordpress.com", "healthline.com", "lowes.com", "washingtonpost.com", "adobe.com", "quizlet.com", "yelp.com", "sharepoint.com", "att.com", "amazonaws.com", "nextdoor.com", "android.com", "linktr.ee", "macys.com", "cnbc.com", "gamerant.com"]
	# check_sites(site_list)
	###################################
	app_list = ["com.linkedin.android", "com.flashkeyboard.leds"]
	###################################
	# save_cookies()
	###################################
	# click_country_dropdown()
	###################################

# init_manual()






def download_files(site_list):
	###################################
	# {"Interval":["Interval is invalid - 2019-12-01--2023-01-31."]}
	# {"Interval":["Interval is invalid - 2020-12-01--2023-01-31."]}
	# {"Interval":["Interval is invalid - 2020-12-01--2023-01-31."]}
	# https://pro.similarweb.com/export/analysis/GetAudienceInterestsTsv?%23&country=840&filter=%5Bobject%20Object%5D&from=2020%7C12%7C01&isCountryChanged&isDurationChanged=false&isWWW=false&isWebSourceChanged=false&isWindow=false&key=linkedin.com&orderBy=RelevancyScore%20desc&to=2023%7C01%7C27&webSource=Total
	###################################
	from_date_traffic 		= "2019%7C12%7C01"
	to_date_traffic 		= "2023%7C01%7C27"
	###################################
	from_date_traffic_sources_overview_data = "2022%7C01%7C01"
	to_date_traffic_sources_overview_data 	= "2022%7C12%7C31"
	###################################
	from_date 		= "2020%7C12%7C01"
	to_date 		= "2023%7C01%7C27"
	###################################
	from_date_desktop_audience_interests 	= "2019%7C12%7C01"
	to_date_desktop_audience_interests 		= "2023%7C01%7C31"
	
	from_date_mobile_audience_interests 	= "2020%7C10%7C01"
	to_date_mobile_audience_interests 		= "2023%7C01%7C31"
	
	from_date_total_audience_interests 		= "2020%7C10%7C01"
	to_date_total_audience_interests 		= "2022%7C12%7C31"
	###################################
	traffic_sources = ["Total", "Desktop", "MobileWeb"]
	###################################
	sleep_from = 0.3
	sleep_to = 1.25
	###################################
	for a, b in enumerate(site_list):
		###################################
		# time.sleep(2)
		# wait_website(b)
		print("auto_sw: wait_website: PASSED")
		# time.sleep(1)
		###################################
		for x in states:
			###################################
			print("auto_sw: check_sites: x: ", x)
			print("auto_sw: check_sites: states[x]: ", states[x])
			###################################
			# time.sleep(3)
			if states[x] == "840":
				for z in traffic_sources:
					print("auto_sw: check_sites: TrafficAndEngagement: UNITED STATES: ", states[x], str(z))
					get_files("https://pro.similarweb.com/widgetApi/TrafficAndEngagement/EngagementOverview/Excel?ShouldGetVerifiedData=false&country="+str(states[x])+"&from="+str(from_date_traffic)+"&includeSubDomains=true&isWindow=false&keys="+str(b)+"&latest=l&timeGranularity=Daily&to="+str(to_date_traffic)+"&webSource="+str(z)+"")
					time.sleep(random.uniform(sleep_from, sleep_to))
					print("auto_sw: check_sites: TrafficSourcesOverview: UNITED STATES: ", states[x], str(z))
					get_files("https://pro.similarweb.com/widgetApi/MarketingMix/TrafficSourcesOverview/Excel?includeSubDomains=true&keys="+str(b)+"&from="+str(from_date_traffic)+"&to="+str(to_date_traffic)+"&country="+str(states[x])+"&timeGranularity=Daily&webSource="+str(z)+"&latest=l&isWindow=false")
					time.sleep(random.uniform(sleep_from, sleep_to))
					print("auto_sw: check_sites: TrafficSourcesOverviewData: UNITED STATES: ", states[x], str(z))
					get_files("https://pro.similarweb.com/widgetApi/MarketingMix/TrafficSourcesOverviewData/Excel?%23&comparedDuration=&country="+str(states[x])+"&filter=&from="+str(from_date_traffic_sources_overview_data)+"&includeSubDomains=true&isCountryChanged&isDurationChanged=false&isWebSourceChanged=false&isWindow=false&keys="+str(b)+"&orderBy=Share%20desc&timeGranularity=Monthly&to="+str(to_date_traffic_sources_overview_data)+"&webSource="+str(z)+"")
					time.sleep(random.uniform(sleep_from, sleep_to))
					print("auto_sw: check_sites: WebDemographics: UNITED STATES: ", states[x], str(z))
					get_files("https://pro.similarweb.com/widgetApi/WebDemographics/WebDemographicsCombined/Excel?keys="+str(b)+"&webSource="+str(z)+"&from="+str(from_date_traffic_sources_overview_data)+"&to="+str(to_date_traffic_sources_overview_data)+"&isWindow=false&country="+str(states[x])+"&includeSubDomains=true")
					time.sleep(random.uniform(sleep_from, sleep_to))
					print("auto_sw: check_sites: GetAudienceInterestsTsv: UNITED STATES: ", states[x], str(z))
					if z == "Desktop":
						get_files("https://pro.similarweb.com/export/analysis/GetAudienceInterestsTsv?%23&country="+str(states[x])+"&filter=%5Bobject%20Object%5D&from="+str(from_date_desktop_audience_interests)+"&isCountryChanged&isDurationChanged=false&isWWW=false&isWebSourceChanged=false&isWindow=false&key="+str(b)+"&orderBy=RelevancyScore%20desc&to="+str(to_date_desktop_audience_interests)+"&webSource="+str(z)+"")
					elif z == "MobileWeb":
						get_files("https://pro.similarweb.com/export/analysis/GetAudienceInterestsTsv?%23&country="+str(states[x])+"&filter=%5Bobject%20Object%5D&from="+str(from_date_mobile_audience_interests)+"&isCountryChanged&isDurationChanged=false&isWWW=false&isWebSourceChanged=false&isWindow=false&key="+str(b)+"&orderBy=RelevancyScore%20desc&to="+str(to_date_mobile_audience_interests)+"&webSource="+str(z)+"")
					elif z == "Total":
						get_files("https://pro.similarweb.com/export/analysis/GetAudienceInterestsTsv?%23&country="+str(states[x])+"&filter=%5Bobject%20Object%5D&from="+str(from_date_total_audience_interests)+"&isCountryChanged&isDurationChanged=false&isWWW=false&isWebSourceChanged=false&isWindow=false&key="+str(b)+"&orderBy=RelevancyScore%20desc&to="+str(to_date_total_audience_interests)+"&webSource="+str(z)+"")
					time.sleep(random.uniform(sleep_from, sleep_to))
				# time.sleep(3)
			###################################
			else:
				print("auto_sw: check_sites: TrafficAndEngagement: states[x]: ", str(x).upper(), states[x])
				get_files("https://pro.similarweb.com/widgetApi/TrafficAndEngagement/EngagementOverview/Excel?ShouldGetVerifiedData=false&country="+str(states[x])+"&from="+str(from_date_traffic)+"&includeSubDomains=true&isWindow=false&keys="+str(b)+"&latest=l&timeGranularity=Daily&to="+str(to_date_traffic)+"&webSource=Desktop")
				time.sleep(random.uniform(sleep_from, sleep_to))
				print("auto_sw: check_sites: TrafficSourcesOverview: states[x]: ", str(x).upper(), states[x])
				get_files("https://pro.similarweb.com/widgetApi/MarketingMix/TrafficSourcesOverview/Excel?includeSubDomains=true&keys="+str(b)+"&from="+str(from_date_traffic)+"&to="+str(to_date_traffic)+"&country="+str(states[x])+"&timeGranularity=Daily&webSource=Desktop&latest=l&isWindow=false")
				time.sleep(random.uniform(sleep_from, sleep_to))
				print("auto_sw: check_sites: TrafficSourcesOverviewData: states[x]: ", str(x).upper(), states[x])
				get_files("https://pro.similarweb.com/widgetApi/MarketingMix/TrafficSourcesOverviewData/Excel?%23&comparedDuration=&country="+str(states[x])+"&filter=&from="+str(from_date_traffic_sources_overview_data)+"&includeSubDomains=true&isCountryChanged&isDurationChanged=false&isWebSourceChanged=false&isWindow=false&keys="+str(b)+"&orderBy=Share%20desc&timeGranularity=Monthly&to="+str(to_date_traffic_sources_overview_data)+"&webSource=Desktop")
				time.sleep(random.uniform(sleep_from, sleep_to))
				print("auto_sw: check_sites: GetAudienceInterestsTsv: states[x]: ", str(x).upper(), states[x])
				get_files("https://pro.similarweb.com/export/analysis/GetAudienceInterestsTsv?%23&country="+str(states[x])+"&filter=%5Bobject%20Object%5D&from="+str(from_date_desktop_audience_interests)+"&isCountryChanged&isDurationChanged=false&isWWW=false&isWebSourceChanged=false&isWindow=false&key="+str(b)+"&orderBy=RelevancyScore%20desc&to="+str(to_date_desktop_audience_interests)+"&webSource=Desktop")
				time.sleep(random.uniform(sleep_from, sleep_to))
			###################################






# https://pro.similarweb.com/widgetApi/TrafficAndEngagement/EngagementOverview/Excel?ShouldGetVerifiedData=false&country=840&from=2019%7C12%7C01&includeSubDomains=true&isWindow=false&keys=linkedin.com&latest=l&timeGranularity=Daily&to=2023%7C01%7C27&webSource=Total
# https://pro.similarweb.com/widgetApi/MarketingMix/TrafficSourcesOverview/Excel?includeSubDomains=true&keys=linkedin.com&from=2019%7C12%7C01&to=2023%7C01%7C27&country=840&timeGranularity=Daily&webSource=Total&latest=l&isWindow=false
# https://pro.similarweb.com/widgetApi/MarketingMix/TrafficSourcesOverview/Excel?includeSubDomains=true&keys=linkedin.com&from=2022%7C01%7C01&to=2022%7C12%7C31&country=8404&timeGranularity=Daily&webSource=Desktop&latest=l&isWindow=false
# https://pro.similarweb.com/widgetApi/MarketingMix/TrafficSourcesOverviewData/Excel?%23&comparedDuration=&country=840&filter=&from=2022|01|01&includeSubDomains=true&isCountryChanged&isDurationChanged=false&isWebSourceChanged=false&isWindow=false&keys=linkedin.com&orderBy=Share%20desc&timeGranularity=Daily&to=2022|12|31&webSource=Desktop
# https://pro.similarweb.com/widgetApi/MarketingMix/TrafficSourcesOverviewData/Excel?%23&comparedDuration=&country=840&filter=&from=2022%7C01%7C01&includeSubDomains=true&isCountryChanged&isDurationChanged=false&isWebSourceChanged=false&isWindow=false&keys=linkedin.com&orderBy=Share%20desc&timeGranularity=Daily&to=2022%7C12%7C31&webSource=Total
# https://pro.similarweb.com/widgetApi/WebDemographics/WebDemographicsCombined/Excel?keys=linkedin.com&webSource=Total&from=2019%7C12%7C01&to=2023%7C01%7C27&isWindow=false&country=840&includeSubDomains=true

# https://pro.similarweb.com/export/analysis/GetAudienceInterestsTsv?%23&country=840&filter=%5Bobject%20Object%5D&from=2019%7C12%7C01&isCountryChanged&isDurationChanged=false&isWWW=false&isWebSourceChanged=false&isWindow=false&key=linkedin.com&orderBy=RelevancyScore%20desc&to=2023%7C01%7C31&webSource=Desktop
# https://pro.similarweb.com/export/analysis/GetAudienceInterestsTsv?%23&country=840&filter=%5Bobject%20Object%5D&from=2020%7C10%7C01&isCountryChanged&isDurationChanged=false&isWWW=false&isWebSourceChanged=false&isWindow=false&key=linkedin.com&orderBy=RelevancyScore%20desc&to=2023%7C01%7C31&webSource=MobileWeb
# https://pro.similarweb.com/export/analysis/GetAudienceInterestsTsv?%23&country=840&filter=%5Bobject%20Object%5D&from=2020%7C10%7C01&isCountryChanged&isDurationChanged=false&isWWW=false&isWebSourceChanged=false&isWindow=false&key=linkedin.com&orderBy=RelevancyScore%20desc&to=2022%7C12%7C31&webSource=Total





def get_files(url):
	# time.sleep(0.5)
	driver.execute_script("window.open('');")
	time.sleep(0.5)
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(0.5)
	print("auto_sw: get_files: url: ", str(url))
	driver.get(url)
	time.sleep(0.5)
	driver.close()
	# time.sleep(0.5)
	driver.switch_to.window(driver.window_handles[0])













def get_ids(filename):
	a = open(filename+".csv", "r", encoding="utf-8", newline="", errors="ignore")
	b = csv.reader(a)
	c = [c[0] for c in b]
	a.close()
	return c


def download_app_files(app_list):
	###################################
	# {"Interval":["Interval is invalid - 2019-12-01--2023-01-31."]}
	# {"Interval":["Interval is invalid - 2020-12-01--2023-01-31."]}
	# {"Interval":["Interval is invalid - 2020-12-01--2023-01-31."]}
	# https://pro.similarweb.com/export/analysis/GetAudienceInterestsTsv?%23&country=840&filter=%5Bobject%20Object%5D&from=2020%7C12%7C01&isCountryChanged&isDurationChanged=false&isWWW=false&isWebSourceChanged=false&isWindow=false&key=linkedin.com&orderBy=RelevancyScore%20desc&to=2023%7C01%7C27&webSource=Total
	###################################
	# from_date_traffic 		= "2019%7C12%7C01"
	# to_date_traffic 		= "2023%7C01%7C27"
	# ###################################
	# from_date_traffic_sources_overview_data = "2022%7C01%7C01"
	# to_date_traffic_sources_overview_data 	= "2022%7C12%7C31"
	# ###################################
	# from_date 		= "2020%7C12%7C01"
	# to_date 		= "2023%7C01%7C27"
	# ###################################
	# from_date_desktop_audience_interests 	= "2019%7C12%7C01"
	# to_date_desktop_audience_interests 		= "2023%7C01%7C31"
	
	# from_date_mobile_audience_interests 	= "2020%7C10%7C01"
	# to_date_mobile_audience_interests 		= "2023%7C01%7C31"
	
	# from_date_total_audience_interests 		= "2020%7C10%7C01"
	# to_date_total_audience_interests 		= "2022%7C12%7C31"
	###################################
	sleep_from = 0.3
	sleep_to = 1.25
	###################################
	for a, b in enumerate(app_list):
		###################################
		# time.sleep(2)
		# wait_website(b)
		print("auto_sw: wait_website: PASSED")
		# time.sleep(1)
		###################################
		# time.sleep(3)
		print("download_app_files: Store Downloads: ", )
		# get_files("https://pro.similarweb.com/widgetApi/TrafficAndEngagement/EngagementOverview/Excel?ShouldGetVerifiedData=false&country="+str(states[x])+"&from="+str(from_date_traffic)+"&includeSubDomains=true&isWindow=false&keys="+str(b)+"&latest=l&timeGranularity=Daily&to="+str(to_date_traffic)+"&webSource="+str(z)+"")
		get_files("https://pro.similarweb.com/api/AppAnnie/StoreDownloads/Excel?%23&changedDuration=true&country=999&device=Total&from=2021%7C12%7C01&isWindow=false&keys="+str(b)+"&store=google&to=2023%7C02%7C28")
		time.sleep(random.uniform(sleep_from, sleep_to))

		print("download_app_files: "+str(b)+": INSTALL BASE")
		get_files("https://pro.similarweb.com/api/AppAnnie/InstallBase/Graph/Excel?%23&country=840&device=Combined&from=2021%7C12%7C01&keys="+str(b)+"&store=google&to=2023%7C02%7C28")
		time.sleep(random.uniform(sleep_from, sleep_to))
		
		print("download_app_files: "+str(b)+": INSTALL BASE GROWTH")
		get_files("https://pro.similarweb.com/api/AppAnnie/InstallBase/Delta/Excel?%23&country=840&device=total&from=2022%7C02%7C01&keys="+str(b)+"&store=google&to=2023%7C02%7C28")
		time.sleep(random.uniform(sleep_from, sleep_to))

		print("download_app_files: "+str(b)+": MONTHLY ACTIVE USERS (MAU) and OPEN RATE")
		get_files("https://pro.similarweb.com/api/AppAnnie/Engagement/Mau/Excel?country=840&from=2021%7C12%7C01&to=2023%7C02%7C28&keys="+str(b)+"&store=google&timeGranularity=Monthly&isWindow=false&device=Combined")
		time.sleep(random.uniform(sleep_from, sleep_to))
		
		print("download_app_files: "+str(b)+": TOTAL SESSIONS")
		get_files("https://pro.similarweb.com/api/AppAnnie/Engagement/Excel?country=840&from=2021%7C12%7C01&to=2023%7C02%7C28&keys="+str(b)+"&store=google&timeGranularity=Monthly&isWindow=false&device=Combined")
		time.sleep(random.uniform(sleep_from, sleep_to))
		
		print("download_app_files: "+str(b)+": RETENTION")
		get_files("https://pro.similarweb.com/api/AppAnnie/Retention/OverTimePerDayExcel?%23&country=840&device=Total&from=2021%7C12%7C01&keys="+str(b)+"&store=google&to=2023%7C02%7C28")
		time.sleep(random.uniform(sleep_from, sleep_to))
		
		print("download_app_files: "+str(b)+": DEMOGRAPHICS")
		get_files("https://pro.similarweb.com/api/AppAnnie/AppDemographics/appsAndCategories/Excel?country=840&from=2021%7C12%7C01&includeSubDomains=true&isWindow=false&keys="+str(b)+"&store=google&timeGranularity=Monthly&to=2023%7C02%7C28")
		time.sleep(random.uniform(sleep_from, sleep_to))
					




def init_headless():
	###################################
	login_url = "https://pro.similarweb.com/"
	get_page(login_url)
	###################################
	# zoom_out()
	# zoom_out()
	# zoom_out()
	###################################
	login()
	###################################
	wait_main_page()
	###################################
	time.sleep(1)
	# zoom_out()
	# time.sleep(0.15)
	# zoom_out()
	# time.sleep(0.15)
	# zoom_out()
	# time.sleep(1)
	###################################
	# site_list = ["linkedin.com", "google.com", "facebook.com", "amazon.com"]
	# download_files(site_list)
	###################################
	app_list = ["com.linkedin.android", "com.flashkeyboard.leds"]
	test_list = get_ids("add_ids_0403_similarwebscroll")
	print(test_list)
	download_app_files(app_list)
	###################################

init_headless()


# driver.execute_script('''window.open("","_blank");''')

# time.sleep(1)
# driver.execute_script("window.open('');")
# time.sleep(1)
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(1)
# driver.get("http://google.com/")
# driver.close()




# time.sleep(1)
# driver.execute_script("window.open('');")
# time.sleep(1)
# driver.execute_script("window.open('about:blank','secondtab');")
# driver.switch_to.window("secondtab")


# driver.execute_script("window.open('about:blank','thirdtab');")
# driver.switch_to.window("thirdtab")
# driver.switch_to.window("secondtab")
# driver.close()
# webBrowser.get('<>')
# body = driver.find_element_by_tag_name("body")
# body.send_keys(Keys.CONTROL, "t")
# body.send_keys(Keys.CONTROL, "t")
# body.send_keys(Keys.CONTROL, "t")
# body.send_keys(Keys.CONTROL, "t")
# body.send_keys(Keys.CONTROL, "t")


# time.sleep(3)
# ActionChains(driver).key_down(Keys.LEFT_CONTROL).send_keys('t').key_up(Keys.LEFT_CONTROL).perform()
# time.sleep(3)
# ActionChains(driver).key_down(Keys.LEFT_CONTROL).send_keys('w').key_up(Keys.LEFT_CONTROL).perform()


# driver.find_element_by_tag_name("body").send_keys(Keys.LEFT_CONTROL + "t")
# driver.find_element_by_tag_name("body").send_keys(Keys.LEFT_CONTROL + "t")
# driver.find_element_by_tag_name("body").send_keys(Keys.LEFT_CONTROL + "t")



# https://pro.similarweb.com/api/AppAnnie/Engagement/Dau/Excel?country=840&from=2021%7C10%7C01&to=2022%7C12%7C31&keys=com.tabtrader.android&store=google&timeGranularity=Monthly&isWindow=false&device=Combined

#     return [x for x in sequence if x