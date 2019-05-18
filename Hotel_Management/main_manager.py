from Hotel_Management.hotel import Hotel

class Hotel_Manager:
	"""
	A class used to represent hotel manager
	"""
	def __init__(self):
		"""
		A method used for initialising hotel manager.
		"""
		self.rooms_num = 10
		self.hotel = Hotel()
		try:
			self.hotel.open()
		except:
			self.hotel.save()
			self.hotel.open()
		self.current_room = None

	def run_command(self, command):
		"""
		A method used to run certain commands for managing hotel.
		Below is list of commands.

		exit: exits from management, save files
		add room : adds room to your hotel
		print rooms: prints room
		manage room: opens rooms managing
		delete room: delete certain room
		:param command:
		:return:
		"""
		if command == "exit":
			self.hotel.save()
			return
		elif command == "add room":
			self.hotel.addroom()
			return
		elif command == "print rooms":
			return self.hotel.watch_rooms()
		elif "manage room" in command:
			num_room = int(command.split()[-1])
			self.current_room = self.hotel.getroom(num_room)
			return
		elif "delete room" in command:
			num_room = int(command.split()[-1])
			self.hotel.delroom(num_room)
			return
		else:
			print("No such command.")
			return 

	def add_booking_to_current_room(self, checkin, checkout,
									price_p_night, additional_costs,
									commission_percent, site):
		"""
		A method used to add booking to current room of hotel.
		:param id_num: int: number of booking
		:param checkin: str: "yyyy-mm-dd"
		:param checkout: str "yyyy-mm-dd"
		:param price_p_night: int : price per night
		:param additional_costs: DynamicArray with additional costs
		:param commission_percent: int
		:param site: str : site where room was booked
		:return:
		"""
		self.current_room.add_booking(checkin, checkout,
				 					  price_p_night,
									  additional_costs,
									  commission_percent,
				 					  site)

	def see_curr_room_bookings(self):
		"""
		A method used to return inf about current room's bookings.
		:return: str
		"""
		return self.current_room.get_str_bookings()

	def curr_room_del_booking(self, num_booking):
		"""
		A method used to delete booking with certain num
		:param num_booking: id of booking - number e.g. 1
		:return:
		"""
		self.current_room.del_booking(num_booking)

	def curr_room_write_calendar(self):
		"""
		Writes calendar of current room.
		:return:
		"""
		self.current_room.print_calendar()

	def exit(self):
		"""
		A method used to exit the programme.
		Saves hotel, rooms to files.
		:return:
		"""
		self.hotel.save()

	def curr_room_add_costs(self, num_booking, name, sum):
		"""
		A method used to add expenses to the booking.
		:param num_booking: int: id number of booking
		:return:
		"""
		self.current_room.add_costs(num_booking, name, sum)





