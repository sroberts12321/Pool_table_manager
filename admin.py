import time
import datetime
import os

#color.RED + "" + color.END

#-------------------------------------------------------------------
#  Model
#-------------------------------------------------------------------

class color:
   PURPLE = '\033[95m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class PoolTable:
	def __init__(self):
		self.occupied = False
		self.name = ""
		self.format_start = None
		self.number = ""

	def __repr__(self):
		return ('%s : %s' % (self.name, self.availability()))
	
	def check_out(self):
		if self.occupied == False:
			self.occupied = True
			self.start_time = time.time()
			self.format_start = datetime.datetime.now().strftime("%H:%M")
			print(f"\t\t  {self.name} has been successfully checked out at {self.format_start}")
			enter_to_continue()
		else:
			print(f"\t\t  {self.name} has already been checked out")
			enter_to_continue()

	def check_in(self, start_time):
		self.start_time = start_time
		self.end_time = time.time()
		self.occupied = False
		if self.start_time is None:
			print("\t\t  That table has not been checked out")
			enter_to_continue()
		else:
			self.elapsed = round((self.end_time - self.start_time), 2)
		self.start_time = None
		self.format_start = None
		
		if self.elapsed >= 3600:
			self.hour = round((self.elapsed/60)/60, 2)
			print(f"\t\t  {self.name} successfully checked in")
			print(f"\t\t  {self.name} was checked out for " + str(self.hour) + " hours")
			enter_to_continue()
		elif self.elapsed >= 60:
			self.min = round(self.elapsed/60, 2)
			print(f"\t\t  {self.name} successfully checked in")
			print(f"\t\t  {self.name} was checked out for " + str(self.min) + " minutes")
			enter_to_continue()
		else:
			print(f"\t\t  {self.name} successfully checked in")
			print(f"\t\t  {self.name} was checked out for " + str(self.elapsed) + " seconds")
			enter_to_continue()

	def table_status(self, start_time):
		self.start_time = start_time
		self.now_time = time.time()
		self.elapsed = round((self.now_time - self.start_time), 2)
		
		if self.elapsed >= 60:
			self.min = round(self.elapsed/60, 2)
			print( f"\t\t  {self.name} has been checked out for " + str(self.min) + " minutes\n\n")
			enter_to_continue()
		else:
			print( f"\t\t  {self.name} has been checked out for " + str(self.elapsed) + " seconds\n\n")
			enter_to_continue()

		# if self.occupied == False:
		# 	print( f"\t\t  {self.name} is available")
		# 	enter_to_continue()
		# elif self.occupied == True:
		# 	print( f"\t\t  {self.name} is currently checked out!")
		# 	enter_to_continue()

	def availability(self):
		if self.occupied == False:
			return f"{self.name} is available"
		elif self.occupied == True:
			return f"{self.name} is checked out"


def enter_to_continue():
	input("\n\t\t    Press enter to continue")

def search_tables(name):
	for table in all_tables:
		if name == table.name:
			return table
		else:
			pass
def search_table_numbers(number):
	for table in all_tables:
		if number == table.number:
			return table
		else:
			pass

#-------------------------------------------------------------------
#  View
#-------------------------------------------------------------------


def line():
	print("-----------------------------------------------------------------------------\n\n")
def write():
 	pass
def options():
	print("-----------------------------------------------------------------------------")
	print("------------------------------     Options     ------------------------------")
	print("-----------------------------------------------------------------------------")
	print("\t\t\t"+color.RED + "rent" + color.END+"         - rent a table")
	print("\t\t\t"+color.RED + "check in" + color.END+"     - check in a table")
	print("\t\t\t"+color.RED + "q" + color.END+"            - quit the program")
	print("\t\t\t"+color.RED + "check status" + color.END+" - check how long a table has been rented")

def table_format():
	print("-----------------------------------------------------------------------------")
	print("------  Table #  --------  Availability  ---------  Time of check out  ------")
	print("-----------------------------------------------------------------------------")
	for index in range(len(all_tables)):
		if all_tables[index].format_start is None:
			if index < 9 :
				print("\t" + all_tables[index].name + "\t\t" + all_tables[index].availability() + "\t\t" + "Not rented")
			else:
				print("\t" + all_tables[index].name + "\t" + all_tables[index].availability() + "\t\t" + "Not rented")
		else:
			if index < 9 :
				print("\t" + all_tables[index].name + "\t\t" + all_tables[index].availability() + "\t\t" + all_tables[index].format_start)
			else:
				print("\t" + all_tables[index].name + "\t" + all_tables[index].availability() + "\t\t" + all_tables[index].format_start)

#-------------------------------------------------------------------
#  Controller
#-------------------------------------------------------------------

count = 1

all_tables = [PoolTable() for i in range(12)]

for obj in all_tables:
	obj.name = "table " + str(count)
	obj.number = str(count)
	count += 1

while True:
	os.system('clear')
	table_format()
	options()
	line()
	user_input = input("\t\t  What would you like to do?: ").lower()

	try:

		if user_input[0] == 'q':
			write()
			break

		elif user_input == "rent" or user_input == "rent table" or user_input == "check out":
			line()
			try:
				check_out_input = str(input("\t\t  What table would you like to rent? ")).lower()
				if len(check_out_input) == 1:
					 table_to_check_out = search_table_numbers(check_out_input)
				else:
					table_to_check_out = search_tables(check_out_input)
				print(table_to_check_out.check_out())
			except AttributeError:
				print("\t\t  That is not a table, try again")
				enter_to_continue()

		elif user_input == "check in" or user_input == "check in table" or user_input == "check table in" or user_input =="return":
			line()
			try:
				check_in_input = str(input("\t\t  What table would you like to check in? ")).lower()
				if len(check_in_input) == 1:
					table_to_check_in = search_table_numbers(check_in_input)
				else:
					table_to_check_in = search_tables(check_in_input)
				print(table_to_check_in.check_in(table_to_check_in.start_time))
			except AttributeError:
				print("\t\t  That table isn't checked out")
				enter_to_continue()

		elif user_input == "check status" or user_input == "check table status" or user_input == "status":
			line()
			check_status_input = str(input("\t\t  Check the status of what table? ")).lower()
			if len(check_status_input) == 1:
				table_to_check_status = search_table_numbers(check_status_input)
			else:
				table_to_check_status = search_tables(check_status_input)
			try:
				print(table_to_check_status.table_status(table_to_check_status.start_time))
			except TypeError:
				print("\t\t  "+ table_to_check_status.availability())
				enter_to_continue()
			except AttributeError:
				print("\t\t  "+ table_to_check_status.availability())
				enter_to_continue()
			except:
				print("\t\t  Your input was invalid")
				enter_to_continue()


		elif user_input == "options":
			options()
			line()
	except:
		print("\t\t  Your input was invalid")



 







# print("-------------------------------------------------------------------")
# print("Pool Table Number")
# print("Start Date Time")
# print("End Date Time")
# print("Total Time Played")
# print("Cost")
# print("-------------------------------------------------------------------")

#-------------------------------------------------------------------
#  Time formatting
#-------------------------------------------------------------------

# start = time.time()
# end = time.time()
# elapsed = end - start

# year-month-day
# ex : 2018-5-9
# current_date = datetime.date.today()
# current_time = datetime.datetime.now()

# print(current_date)

# print(current_time)
