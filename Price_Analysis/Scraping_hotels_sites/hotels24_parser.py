# file: hotels24_parser.py
# The file consists function to parse prices on hotels24.com

import urllib.request
from bs4 import BeautifulSoup
import requests
from datetime import datetime


def get_html(city_name):
	'''
	(str) -> html

	:param: city_name: name of city.

	This is function for getting html page from the site. Url - is the
	address of the site.
	'''

	# gets json of autocomplete which contains id of city.
	j = requests.get("https://hotels24.ua/ajax.php?s={}&e=ac&target=universalCompleter&lang_code=en".format(city_name)).json()["result"][1]['cities'][0]
	city_id = j['cityId']
	weight = j['weight']
	cityName = j['cityName'].split(",")

	date = str(datetime.today()).split(' ')
	year = date[0].split("-")[0]
	month = date[0].split("-")[1]
	day = date[0].split("-")[2]

	dateArrival = "{}.{}.{}".format(day, month, year)
	dateDeparture = "{}.{}.{}".format(int(day) + 1, month, year)

	city = "{}%2C+{}+region%2C+{}+".format(cityName[0].strip(),
										   cityName[1].strip(),
										   cityName[2].strip())
	datePicker = "{}+-+{}".format(dateArrival, dateDeparture)

	source = "https://hotels24.ua/?target=search&event=hotel&city_id={}&storeDateInCookie=1&typeLink=hotels24&geoLandingId=&dateArrival=&dateDeparture=&city={}+&datePicker=&max_persons=&lang_code=en".format(city_id, city)
	response = urllib.request.urlopen(source)
	return response.read()


def parse(html):
	'''
	(html) -> list

	This function parses the site and returns list with dicts which
	contains prices for hotels.
	'''
	# soup is the object which helps to find inf on the web page.
	soup = BeautifulSoup(html, 'html.parser')
	# next variable defines table with results of parsing the part
	# of site with teg("div" and id - "superPaginatorDiv"
	table = soup.find("div", id="superPaginatorDiv")
	# table.find_all... це значки ціни на сайті, вони складаються
	# з двох інших підзначків.
	prices_list = []
	# ^ it is the list with dicts which contain prices
	for price_tag in table.find_all("div", class_="hotel-price"):
		price = price_tag.find_all("a")
		prices_list.append(price[0].span.text)
	return prices_list
	#I will live it there for understanding print(table.prettify())

def run_scrapping_24(city_name):
	"""
	A function used to scrape information from hotels24.com
	:param: city_name: str
	:return: lst
	"""
	return parse(get_html(city_name))
