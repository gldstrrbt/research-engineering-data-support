from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv, time


# initialize the webdriver
driver 	= webdriver.Chrome(executable_path=r"./chromedriver.exe")


def gather_listings():
	# get all visible job listings
	job_listings = get_visible_job_listings()

	# create a list to store the scraped data
	data = []

	# loop through the job listings
	for job in job_listings:
		# find the title of the job
		title = job.text

		# find the link to the job listing
		link = job.get_attribute("href")

		# add the scraped data to the data list
		data.append([title, link])
	
	# return the collected listing titles and urls  
	return data


def write_csv(dataset):
	# write the scraped data to a .csv file
	with open("job_listings.csv", "w", newline="", encoding="utf8", errors="ignore") as file:
		writer = csv.writer(file)
		writer.writerow(["Title", "Link"])
		writer.writerows(dataset)


def get_job_count():
	# wait until the job count text/element appears/loads in page
	element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '.job-list-count'))
	WebDriverWait(driver, 60).until(element_present)

	# get job count element
	job_listings = driver.find_element_by_css_selector(".job-list-count")
	# print("get_job_count: job_listings.text: ", job_listings.text)

	# split the text by space and convert to number
	job_listings = int(job_listings.text.split(" ")[0])
	# print("get_job_count: job_listings: ", job_listings)

	# have function/def return the count for number of job listings
	return job_listings


def get_visible_job_listings():
	# find all loaded/visible job listings
	job_listings = driver.find_elements_by_css_selector("h2.job-list-job-title a")

	# have function/def return all job listings
	return job_listings


def scroll_to_bottom(job_count):
	# get number of visible job listings
	num_visible_listings = len(get_visible_job_listings())
	
	# keep scrolling until the number of visible/loaded listings equals the total job count
	while num_visible_listings < job_count:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		num_visible_listings = len(get_visible_job_listings())
		print("scroll_to_bottom: num_visible_listings: ", num_visible_listings)


def init():
	# navigate to the website
	driver.get("https://careers.night.co/jobs")
	time.sleep(1)
	
	# store job count in variable
	job_count = get_job_count()
	print("init: job_count: ", job_count)
	
	# scroll to bottom of page to keep loading more job postings
	scroll_to_bottom(job_count)

	# store collected listings in variable
	collected_listings = gather_listings()

	# write collected listings to csv file
	write_csv(collected_listings)

	# close the webdriver
	driver.quit()


init()