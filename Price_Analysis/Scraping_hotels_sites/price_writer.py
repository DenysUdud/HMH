# file: price_writer
# file consists function for writing inf to json
import json


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

	sum = 0
	for p in main_dict["lower than average price"]:
		sum += int(p)
	average_lower = round(sum / len(main_dict[
										"lower than average price"]))
	main_dict["average_lower"] = average_lower

	sum = 0
	for p in main_dict["higher than average price"]:
		sum += int(p)
	average_higher = round(sum / len(
		main_dict["higher than average price"]))
	main_dict["average_higher"] = average_higher

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
	the_most_pop_count = 0
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
