# file: terminal_interface.py
# file consists function for making terminal interface for running
# scraping

from Price_Analysis.Scraping_hotels_sites.main_scrap import main_scrap
import json
import matplotlib.pyplot as plt

def run_scrap_terminal():
	"""
	A function used to run scrapping programme in the terminal.
	:return: None
	"""
	print("💹 You are in Price Analysis menu. 💹\n",
		  "⬇️ To run an analysis of your local hotels - type "
		  "requested data below (if you do not want mention stars "
		  "and type of accommodation - enter '-') ⬇️")

	# definition whether
	definit = False
	while definit is False:
		try:
			city_name = input("Enter name of city: ").strip()
			# city_size = int(input("Enter size of your city
			# (1 <= value <= 10): "))

			city_size = 6
			stars = input("Enter the number of stars hotel/room "
						  "should have to be analysed (1-5): ")
			if stars != "-":
				int(stars)
			print("Examples: apartment, hotel, hostel, guest_house, "
				  "aparthotel, villa, motel")
			tyo = input("Enter type of accommodation which will"
						" be analysed (examples above ⬆️): ").strip()
			if check_name(city_name) and tyo in {"apartment", "hotel",
												 "hostel",
												 "guest_house",
												 "aparthotel",
												 "villa",
												 "motel", "-"}:
				definit = True
			if definit is False:
				raise BaseException
		except BaseException:
			print("❌ You entered something wrong, try again ❌:")

	print("🔄 Starting analyse 🔄")

	# start analyse
	file_name = main_scrap(city_name, stars, tyo, city_size)
	with open(file_name, "r") as file:
		data = json.load(file)

		# print(data)

		print("📊 There is results of analysys 📊")
		print("Average price: {}".format(round(int(data[
										'average']))
										 ))
		print("The most popular price: {}".format(data[
										"the most popular price"]))
		print("Average among low prices: {}".format(data[
												"average_lower"]))
		print("Average among high prices: {}".format(data[
												"average_higher"]))
		more = input("To see more details type 'more': ").strip()
		if more == 'more':
			print('⬇️ Lower than average price ⬇️')
			string = ""
			
			# reads obligatory вфеф акщь сім ашдую
			for i, p in enumerate(data['lower than average price']):
				string += str(p) + ", "
				if i % 20 == 0 and i != 0:
					print(string)
					string = ""
			if len(string) < 19:
				print(string)

			string = ''
			print('\n⬇️ Higher than average price ⬇️')
			for i, p in enumerate(
					data['higher than average price']):
				string += str(p) + ", "
				if i % 20 == 0 and i != 0:
					print(string)
					string = ""
			if len(string) < 19:
				print(string)

			print('\n⬇️ Average prices ⬇️')
			print(data['average prices'])

			lst = []
			print('\n⬇️ Prices mode ⬇️')
			for key in data['prices mode']:
				tup = (int(key), "{} times | ".format(
					data['prices mode'][key]))
				lst.append(tup)
			lst.sort(key=lambda x: x[0])

			string = ""

			for i, tup in enumerate(lst):
				string += "{} - {}".format(tup[0], tup[1])
				if i % 20 == 0 and i != 0:
					print(string)
					string = ""
			print(string)

			# built mode graphic
			x_lst = []
			y_lst = []

			for key in data['prices mode']:
				x_lst.append(int(key))
				y_lst.append(int(data['prices mode'][key]))

			plt.bar(x_lst, y_lst,
					label="Frequency of price \noccurrence",
					color='g', width=100)
			plt.xlabel("Price per night")
			plt.ylabel("Frequency of occurrence")
			plt.title("Graph of mode")
			plt.legend()
			plt.show()
		return 
			

def check_name(name):
	"""
	A function used to check name of city.
	If it contains not alpha - returns False.
	:param name: str
	:return: bool
	"""
	for let in name:
		if let.isalpha() is False:
			return False
	return True

