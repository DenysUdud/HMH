# file: hotelscan_parser
# module consists functions for parsing hotelscan.com (site with
# your dream hotel at the best price).

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime


def hotelscan_parser(city_name, rooms, stars, toa, size):
	"""
	A function used to parse the HotelScan sited and return prices
	in lists of list.

	Also writes results to file: prices_hotelscan.txt

	example of return: [['618', 'грн'], ['677', 'грн'],
						['648', 'грн', '648', 'грн', '648', 'грн']
	:param city_name: name of city: str
	:param rooms: number of rooms: int
	:param stars: number of stars (1-5): int
	:param toa: class of room: str (possible: apartment, hotel,
									hostel, guest_house, aparthotel,
									villa, motel)
	:param size: size of the city in measures from 1 to 10.

	:return: list
	"""
	# send autocomplete request and gets id of city
	id = requests.get('https://hotelscan.com/autocomplete?q=%7B%22locale%22%3A%22en%22%2C%22term%22%3A%22{}%22%2C%22pos%22%3A%22ua%22%7D'.format(city_name)).json()['suggest'][0]['hs_id']

	# make driver to parse dynamic page
	driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

	all_prices = []

	#  generate date for request
	date = str(datetime.today()).split(' ')
	year = date[0].split("-")[0]
	month = date[0].split("-")[1]
	day = date[0].split("-")[2]

	checkin = "{}-{}-{}".format(year, month, day)
	checkout = "{}-{}-{}".format(year, month, int(day) + 1)

	if size == 0:
		count = 1
	elif size <= 3:
		count = 2
	elif 3 < size <= 5:
		count = 5
	elif 5 < size <= 8:
		count = 10
	else:
		count = 17

	# parse different pages of site
	old_source = None
	for num_page in range(count):
		# format driver and gets source
		if stars is not "-" and toa is not "-":
			driver.get("https://hotelscan.com/en/search?geoid={}&checkin={}&checkout={}&page={}&rooms=2&stars={}&toa={}".format(
				id, checkin, checkout, num_page, stars, toa))
		elif stars is "-" and toa is not "-":
			driver.get("https://hotelscan.com/en/search?geoid={}&checkin={}&checkout={}&page={}&rooms=2&toa={}".format(
				id, checkin, checkout, num_page, toa))
		elif stars is not "-" and toa is "-":
			driver.get("https://hotelscan.com/en/search?geoid={}&checkin={}&checkout={}&page={}&rooms=2&stars={}".format(
				id, checkin, checkout, num_page, stars))
		elif stars is "-" and toa is "-":
			driver.get("https://hotelscan.com/en/search?geoid={}&checkin={}&checkout={}&page={}&rooms=2".format(
				id, checkin, checkout, num_page))

		source = driver.execute_script("return document.documentElement.outerHTML")
		if old_source == source:
			break
		old_source = driver.execute_script("return document.documentElement.outerHTML")


		# make soup to work with
		soup = BeautifulSoup(source, features="html.parser")
		property_list = soup.find("section", id="property-list")

		for info_deals in property_list.find_all(class_="info-deals"):
			deals = info_deals.find(class_="deals")
			price = deals.find_all(class_="currency-value")
			price_list = []
			for el in price:
				price_list.append(el.text)
			all_prices.append(price_list)
	driver.quit()

	# write prices to the file
	with open('prices_hotelscan.txt', 'w') as f:
		for item in all_prices:
			f.write("%s\n" % item)

	return all_prices


def clean_results(lst):
	"""
	A function used to write prices of hotels in right form
	(currency - hryvnya, without bugs).
	Example of return: [200, 400, 500]
	:param lst: list
	:return: list
	"""
	main_lst = []
	for price in lst:
		if price is not None and len(price) > 0:
			val = price[0]
			curr = price[1]
			if curr is "usd":
				main_lst.append(int(val)*26)
			else:
				main_lst.append(int(val))
	return main_lst


def run_scrapping_scan(city_name, rooms, stars, toa, size):
	"""
	A function used to run parsing. Returns sorted list with prices
	in hryvnya (1 hryvnya= 26 usd)

	:param city_name: name of city: str
	:param rooms: number of rooms: int
	:param stars: number of stars (1-5): int
	:param toa: class of room: str (possible: apartment, hotel,
									hostel, guest_house, aparthotel,
									villa, motel)
	:param size: size of the city in measures from 1 to 10.

	:return: list
	"""
	return clean_results(hotelscan_parser(city_name, rooms,
											stars, toa, size))
