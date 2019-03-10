import urllib.request
from bs4 import BeautifulSoup
import math
import json


def get_html(url):
	'''
	(str) -> html

	This is function for getting html page from the site. Url - is the
	address of the site.
	'''
	response = urllib.request.urlopen(url)
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


def json_maker(prices_list):
	'''
	(list) -> str
	This function returns json file with analyzed prices.
	'''
	main_dict = {}
	main_dict["lower than average price"] = []
	main_dict["higher than average price"] = []
	main_dict["average prices"] = []

	sum = 0
	prices_list = [int(price) for price in prices_list]

	for price in prices_list:
		sum += price

	average_price = sum/len(prices_list)
	bottom_average = average_price - (average_price % 10) - 100
	peak_average = average_price - (average_price % 10) + 100
	mode_results = mode(prices_list)
	main_dict["average"] = average_price
	main_dict["the most popular price"] = mode_results[1]
	main_dict["prices mode"] = mode_results[0]
	main_dict["median"] = median(prices_list)

	for price in prices_list:
		if price < bottom_average:
			main_dict["lower than average price"].append(price)
		elif price > peak_average:
			main_dict["higher than average price"].append(price)
		else:
			main_dict["average prices"].append(price)
	with open("statistic_price.json", "w", encoding="UTF-8") as f:
		json.dump(main_dict, f)
	return "statistic_price.json"


def mode(lst):
	'''
	(list) -> dict, int
	This function returns mode of list in type of dict and the
	most popular price.
	'''
	main_dict = {}
	the_most_pop_price = 0
	the_most_pop_count  = 0
	for price in lst:
		count = lst.count(price)
		if price not in main_dict.keys():
			main_dict[price] = count
		if count > the_most_pop_count:
			the_most_pop_price = price
	return main_dict, the_most_pop_price


def median(lst):
	'''
	(lsit) -> int
	This function returns the median of list.
	'''
	lst.sort()
	lenght = len(lst)
	if lenght % 2 == 0:
		med = (lst[int(lenght / 2)] + lst[int(lenght / 2 - 1)]) // 2
	else:
		med = lst[int(lenght // 2)]
	return med


# def get_more_hotels(html):
# 	soup = BeautifulSoup(html, 'html.parser')
# 	soup.find("div", class_="super-paginator-child")
# 	print(soup.find("a", onclick="paginatorManager.setShowNextPart()"))


def main():
	'''
	This is the main fumction.
	:return:
	'''
	url = "https://hotels24.ua/?target=search&event=hotel&storeDateInCookie=1&typeLink=hotels24&max_persons=2&city_id=18400&order_hotel=&lang_code=en&dateArrival=&dateDeparture=&radius=5&openMap=0&city=Truskavets%2C+Lviv+region%2C+Ukraine+&datePicker=&places_filter=0&place_filter="
	html = get_html(url)
	prices_list = parse(html)
	json_maker(prices_list)
	# get_more_hotels(html)

main()