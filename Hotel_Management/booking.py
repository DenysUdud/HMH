# file: booking.py
from datetime import datetime, timedelta

class Booking:
	"""
	A class used to represent booking.
	"""
	def __init__(self, name, checkin, checkout, checkin_hour,
				 price_p_night, additional_costs,
				 commission_percent, site):
		"""
		A method used to initialise booking.
		:param checkin: date of checkin in form: 'yyyy-mm-dd'
		:param checkout: date of checkout in form: 'yyyy-mm-dd'
		:param checkin_hour:
		:param price_p_night: int
		:param additional_costs: Array
		"""
		self._name = name
		self.checkin = checkin
		self.checkout = checkout
		self.checkin_hour = checkin_hour
		self._price_p_night = price_p_night
		self._additional_costs = additional_costs
		self.site = site
		self.commission_percent = commission_percent
		self.status = self.get_status()
		self.num_days = self.get_numdays(checkin, checkout)
		self.income = self.get_income()
		self.add_cost("Commission", self.get_commission())

	def get_checkin(self):
		"""
		A method used to get checkin date
		:return: str
		"""
		return self.checkin

	def get_checkout(self):
		"""
		A method used to return checkout date
		:return:
		"""
		return self.checkout

	def get_name(self):
		"""
		A method used to return name of booking.
		:return: str
		"""
		return self._name

	def get_status(self):
		"""
		A method used to get status of booking. If today is date
		between checkin and checkout date - returns True.
		:return: bool
		"""
		today = str(datetime.today())
		tup = self.get_date_inf(today.split(" ")[0])
		tod_year = tup[0]
		tud_month = tup[1]
		tud_day = tup[2]
		hour = today.split()[1].split(":")[0]

		# get checkin date inf and checkout date inf
		tup = self.get_date_inf(self.checkin)
		in_year = tup[0]
		in_month = tup[1]
		in_day = tup[2]

		tup = self.get_date_inf(self.checkout)
		out_year = tup[0]
		out_month = tup[1]
		out_day = tup[2]

		if in_year <= tod_year <= out_year and\
			in_month <= tud_month <= out_month:
			if in_day < tud_day < out_day:
				if hour < self.checkin_hour:
					return True
				else:
					return False
			elif in_day > tud_day and tud_month > in_month:
				if int(hour) < self.checkin_hour:
					return True
				else:
					return False
			else:
				return False

	def get_numdays(self, date_1, date_2):
		"""
		A function used to get sum of all dates
		between two dates - 1.
		:param date_1: str: "yyyy-mm-dd"
		:param date_2: str: "yyyy-mm-dd"
		:return: int
		"""
		tup = self.get_date_inf(self.checkin)
		year_1 = int(tup[0])
		month_1 = int(tup[1])
		day_1 = int(tup[2])

		tup = self.get_date_inf(self.checkout)
		year_2 = int(tup[0])
		month_2 = int(tup[1])
		day_2 = int(tup[2])

		start = datetime(year_1, month_1, day_1, 0, 0, 0)
		end = datetime(year_2, month_2, day_2, 0, 0, 0)
		delta = end - start
		lst = []

		for i in range(delta.days + 1):
			lst.append(start + timedelta(days=i))

		return len(lst) - 1

	@staticmethod
	def get_date_inf(date_str):
		"""
		A method used to get information about str from str date
		in format 'yyyy-mm-dd'
		:param date_str:
		:return: tuple
		"""
		year = date_str.split("-")[0]
		month = date_str.split("-")[1]
		day = date_str.split("-")[2]
		return year, month, day

	def get_income(self):
		"""
		A method used to get income.
		:return: int
		"""
		return self._price_p_night * self.num_days

	def get_commission(self):
		"""
		A method used to get money which will be payed as commission.
		:return: int
		"""
		return self.commission_percent * self.income / 100

	def add_cost(self, name, price):
		"""
		A method used to add additional costs.
		:param name: str : name of add cost
		:param price: int: price of add cost
		:return:
		"""
		self._additional_costs.append(Additional_cost(name, price))

	def get_price(self):
		"""
		A method returns price per night
		:return:
		"""
		return self._price_p_night

	def get_costs_inf(self):
		"""
		A method used to return information about
		all costs in str form.
		:return: str
		"""
		string = ""
		add_costs = self._additional_costs
		for add_cost in add_costs:
			string += "{} - {}; ".format(add_cost.get_name(),
									  add_cost.get_cost())
		return string

	def get_sum_costs(self):
		"""
		A method returns sum of all additional costs.
		:return: None
		"""
		add_costs = self._additional_costs
		sum = 0
		for add_cost in add_costs:
			sum += int(add_cost.get_cost())
		return sum

	def get_revenue(self):
		"""
		A method used to return revenue.
		:return: int
		"""
		return self.get_income() - self.get_sum_costs()

	def get_str(self):
		"""
		A method used to return information about booking in str
		form.
		id, checkin, checkout, num_days, price_per_night, site, revenue, cost [additional cost1; additional cost2 ...]
		:return: str
		"""
		if self.status is True:
			stat = "active"
		else:
			stat = "not active"
		string_1 = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, [{}]".format(
			self._name, stat,
			self.checkin, self.checkout, self.num_days,
			self._price_p_night, self.site, self.commission_percent,
			self.get_income(),
			self.get_revenue(), self.get_sum_costs(),
			self.get_costs_inf()
		)
		return string_1



class Additional_cost:
	"""
	A class used to represent additional cost.
	"""
	def __init__(self, name, cost):
		"""
		:param name:
		:param cost:
		"""
		self._name = name
		self._cost = cost

	def get_name(self):
		return self._name

	def get_cost(self):
		return self._cost