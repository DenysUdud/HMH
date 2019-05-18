# file: hotel.py
# file contains class for representing Hotel
from Hotel_Management.room import Room
import csv


class Hotel:
	"""
	A class used to represent hotel.
	"""
	def __init__(self):
		self._rooms = []
		self._num_rooms = 0
		for i in range(self._num_rooms):
			self._rooms.append(Room(i))

	def getroom(self, num):
		"""
		A method used to get certain room of hotel
		:param num: int
		:return: object
		"""
		return self._rooms[num - 1]

	def save(self):
		"""
		A method used to save hotel to file.
		:return: str
		"""
		with open("hotel.csv", "w", encoding="UTF-8") as file:
			file.write("name_room\n")
			for i, room in enumerate(self._rooms):
				file.write(self._rooms[i].write_room() + "\n")
				room.write_room()

	def open(self):
		"""
		A method used to open hotel.
		:return:
		"""
		with open("hotel.csv", "r", encoding="UTF-8") as csv_file:
			csv_reader = csv.DictReader(csv_file)
			line_count = 0
			for row in csv_reader:
				if line_count != 0:
					self.addroom()
					self._rooms[line_count].read_room()
					line_count += 1

	def addroom(self):
		"""
		A method used to add rooms to the hotel.
		:return:
		"""
		self._rooms.append(Room(self._num_rooms + 1))
		self._num_rooms += 1

	def delroom(self, num):
		"""
		A method used to delete certain room from hotel
		:param num: int
		:return:
		"""
		for i in range(self._num_rooms):
			if i == num - 1:
				self._rooms.__delitem__(i)

	def watch_rooms(self):
		"""
		A method returns str with all rooms.
		:return: str
		"""
		string = ""
		for i, room in enumerate(self._rooms):
			string += str("Room {} ".format(i+1))

		return string
