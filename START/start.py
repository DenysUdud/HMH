from Price_Analysis.Information_visualisation.terminal_interface import run_scrap_terminal
from Hotel_Management.main_manager import Hotel_Manager
from Hotel_Management.data_structures.arrays import DynamicArray


class MainMenu:
	"""
	A class used to represent hotel
	"""
	def __init__(self):
		"""
		A method used to manage programme.
		"""
		try:
			self.manager = Hotel_Manager()
		except BaseException:
			Hotel_Manager()


	def start(self):
		"""
		A function used to start the HMH programme.
		:return:
		"""
		ident = True
		print("🏠Welcome to HMH (Hotel Manager Helper) main menu🏘️\n",
				"⬇️ Here is menus of programme ⬇️")
		while ident is True:
			print("Price Analysis   |    Manage Hotel   |   Quit")
			menu = input("Enter menu: ")

			if menu.strip() == "Price Analysis":
				run_scrap_terminal()

			if menu.strip() == "Quit":
				self.manager.exit()
				ident = False

			elif menu.strip() == "Manage Hotel":

				quit = False
				while quit is False:
					print("\nYou are in Manage Hotel\nChoose" +\
						  " command :\nexit\nadd room\nprint " +\
						  "rooms\n" +\
						  "manage room\ndelete room\n")
					command = input("Enter command: ").strip()
					if command == "print rooms":
						string = self.manager.run_command(command)
						print(string)
					elif command == "exit":
						self.manager.run_command(command)
						quit = True
					elif command in "add room":
						self.manager.run_command(command)
					elif command in "delete room":
						num = input("Enter number (id) of room: ")
						self.manager.run_command(
							command + " {}".format(num))

					elif "manage room" in command:
						quit_1 = False
						num = input("Enter number (id) of room: ")
						try:
							self.manager.run_command(
								command + " {}".format(num))
						except IndexError:
							print("No such room in your hotel!")
							break
						while quit_1 is not True:
							print("Enter what action you " +
								  "want to do with room {}:".format(
									  self.manager.current_room._name)
								  )
							print("add booking to current room | " +
								  "see current room's bookings | current room show calendar\n" +
								  "current room del booking | cur" +
								  "rent room add expenses | quit")
							command = input("Enter command: ").strip()
							if command == "add booking to current room":
								checkin = input("Enter checkin date in format yyyy-mm-dd: ").strip()
								checkout = input("Enter checkout date in format yyyy-mm-dd: ").strip()
								price_p_night = int(input("Enter price per night: "))
								additional_costs = DynamicArray()
								commission_percent = int(input("Enter comission: "))
								site = input("Enter name of site: ")
								self.manager.add_booking_to_current_room(
									checkin, checkout,
									price_p_night, additional_costs, commission_percent,
									site)
								print("New booking was added")
							elif command == "see current room's bookings":
								print(self.manager.see_curr_room_bookings())
							elif command == "current room del booking":
								num = int(input("Enter id of booking you want delete: "))
								self.manager.curr_room_del_booking(num)
							elif command == "current room show calendar":
								self.manager.curr_room_write_calendar()
							elif command == "current room add expenses":
								id_book = int(input("Enter id of booking: "))
								name = input("Enter name of expense: ").strip()
								price = input("Enter expenses: ")
								self.manager.curr_room_add_costs(id_book,
																 name,
																 price)
							elif command == "quit":
								quit_1 = True
			elif menu.strip() == "Statistic":
				pass

if __name__ == "__main__":
	menu = MainMenu()
	menu.start()