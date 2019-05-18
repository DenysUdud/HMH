# file: room.py
# file contains class Room used to manage and represent room.
from Hotel_Management.data_structures.node import Node
from Hotel_Management.booking import Booking
from Hotel_Management.calendar_builder import plot_calendar
from datetime import datetime, timedelta
import csv


class Room:
	"""
	A class used to represent and manage room.
	"""
	def __init__(self, rooms_num):
		"""
		A method used to initialise room.
		:param rooms_num: int
		"""
		self._name = "Room {}".format(rooms_num)
		self._head = self._current = None
		self._num_bookings = 0
		self._costs = 0
		self._income = 0

	def add_booking(self, checkin, checkout,
				 price_p_night, additional_costs, commission_percent,
				 site):
		"""
		A method used to add bookings to the list.
		:return:
		"""
		name = "id: {}".format(self._num_bookings + 1)

		# defines booking
		booking = Booking(name, checkin, checkout, 12,
						  price_p_night, additional_costs,
						  commission_percent, site)

		# create new node for representing booking
		newNode = Node(item=booking, next=None)

		if self._num_bookings == 0:
			self._head = newNode
		else:
			self._current.next = newNode
		self._current = newNode
		self._num_bookings += 1

	def del_booking(self, num_booking):
		"""
		A method used to delete booking.
		:param booking: object Booking
		:return:
		"""
		name = "id: {}".format(num_booking)

		# crete pointer to run throug the file
		pointer = self._head

		# run trough the file
		while pointer is not None:
			if pointer.item.get_name() == name:
				if pointer is self._head:
					self._head = pointer.next
				else:
					pointer.previous.next = pointer.next
				self._num_bookings -= 1
				return
			pointer = pointer.next
		raise IndexError("There is not such booking")

	def find_booking(self, id_num):
		"""
		A method used to return booking of certain id.
		:param id_num: id of booking. -
		"id: {}".format(self._num_bookings + 1)
		:return:
		"""
		name = "id: {}".format(id_num)
		pointer = self._head
		while pointer is not None:
			if pointer.item.get_name() == name:
				return pointer.item
			pointer = pointer.next
		raise IndexError("There is not such booking")

	@staticmethod
	def get_days_between(date_1, date_2):
		"""
		A function used to get all dates between two dates.
		Returns two lists. One list with days and another with
		months.
		example:
		get_days_between("2019-05-17", "2019-06-04")
		result:
		([17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
		31, 1, 2, 3, 4],
		[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6])

		:param date_1: str: "yyyy-mm-dd"
		:param date_2: str: "yyyy-mm-dd"
		:return: list, list
		"""
		year_1 = int(date_1.split("-")[0])
		month_1 = int(date_1.split("-")[1])
		day_1 = int(date_1.split("-")[2])

		year_2 = int(date_2.split("-")[0])
		month_2 = int(date_2.split("-")[1])

		day_2 = int(date_2.split("-")[2])
		start = datetime(year_1, month_1, day_1, 0, 0, 0)
		end = datetime(year_2, month_2, day_2, 0, 0, 0)

		delta = end - start
		lst_days = []
		lst_month = []
		for i in range(delta.days + 1):
			date = start + timedelta(days=i)
			lst_month.append(int(str(date).split("-")[1]))
			lst_days.append(
				int(str(date).split("-")[2].split(" ")[0]))
		return lst_days, lst_month

	def print_calendar(self):
		"""
		A method used to build calendar of bookings.
		:return:
		"""
		# creates two lists for writing days and months
		days_lst = []
		month_lst = []

		pointer = self._head
		# go trough bookings
		while pointer is not None:
			# yyyy-mm-dd
			# gets all days between checkin and checkout
			between = self.get_days_between(pointer.item.get_checkin(),
											pointer.item.get_checkout())
			days = between[0]
			months = between[1]

			days_lst += days
			month_lst += months
			pointer = pointer.next
		# build calendar
		plot_calendar(days_lst, month_lst)

	def add_costs(self, id_num, name, sum):
		"""
		A method used to add costs to booking.
		:param name: str: name of cost
		:param sum: int: price of offer
		:return: None
		"""
		booking = self.find_booking(id_num)
		booking.add_cost(name, sum)

	def get_str_bookings(self):
		"""
		A method used to get bookings in str form.
		checkin, checkout, num_days, price_per_night, site,
		revenue, cost, [additional cost1; additional cost2 ...],
		:return: str
		"""
		string_1 = "id, status, checkin, checkout, num_days, " +\
				 "price_per_night, site, commission, income, revenue, cost, " +\
				 "additional costs\n"
		pointer = self._head
		while pointer is not None:
			string_1 += pointer.item.get_str() + "\n"
			pointer = pointer.next
		return string_1

	def write_room(self):
		"""
		A method used to save information about room in file with
		name : "name_room.csv" . Also returns name of file.
		:return: str
		"""
		file_name = "{}.csv".format(self._name)
		with open(file_name, "w", encoding="UTF-8") as file:
			file.write(self.get_str_bookings())
		return file_name

	def read_room(self):
		"""
		A method used to read information about room from file with
		name : "name_room.csv"
		:return:
		"""
		file_name = "{}.csv".format(self._name)
		with open(file_name, "r", encoding="UTF-8") as csv_file:
			csv_reader = csv.DictReader(csv_file)
			line_count = 0
			for row in csv_reader:
				if line_count != 0:
					self.add_booking(row["id"], row["checkin"],
									 row["checkout"],
									 row["price_p_night"],
									 row["additional_costs"],
									 row["commission_percent"],
									 row["site"]
									 )
					self.add_booking()
				line_count += 1
