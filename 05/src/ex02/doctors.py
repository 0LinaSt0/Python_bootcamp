import threading
import logging
from time import sleep
from concurrent.futures import ThreadPoolExecutor

DOCTORS_NUMBER = 5
FIRST_DOCTOR_NO = 9

class Doctor:
	def __init__(self, doctor_no):
		self.no = doctor_no


	def use_two_screwdrivers(self, right_screwdriver, left_screwdriver):
		sleep(1)
		if no % 2 == 0:
			right_screwdriver.grab_screwdriver(self.no)
			left_screwdriver.grab_screwdriver(self.no)
			logging.info("Doctor %s: BLAST!", self.no)
			right_screwdriver.release_screwdriver(self.no)
			left_screwdriver.release_screwdriver(self.no)
		else:
			left_screwdriver.grab_screwdriver(self.no)
			right_screwdriver.grab_screwdriver(self.no)
			logging.info("Doctor %s: BLAST!", self.no)
			left_screwdriver.release_screwdriver(self.no)
			right_screwdriver.release_screwdriver(self.no)


class Screwdriver:
	def __init__(self, screwdriver_no):
		self.no = screwdriver_no
		self.screwdriver_lock = threading.Lock()


	def grab_screwdriver(self, doctor_no):
		self.screwdriver_lock.acquire()
		logging.debug("screwdriver#%s GREBED by doctor#%s", self.no,  doctor_no)


	def release_screwdriver(self, doctor_no):
		logging.debug("screwdriver#%s RELEASED by doctor#%s", self.no, doctor_no)
		self.screwdriver_lock.release()


if "__main__" == __name__:
	my_format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=my_format, level=logging.INFO, datefmt="%H:%M:%S")
	# Show all steps
	#logging.getLogger().setLevel(logging.DEBUG)

	doctors = [Doctor(no) for no in range(FIRST_DOCTOR_NO, (FIRST_DOCTOR_NO + DOCTORS_NUMBER + 1))]
	screwdrivers = [Screwdriver(no) for no in range(FIRST_DOCTOR_NO, (FIRST_DOCTOR_NO + DOCTORS_NUMBER + 1))]

	with ThreadPoolExecutor(max_workers=DOCTORS_NUMBER) as executor:
		for no in range(DOCTORS_NUMBER):
			left_screwdriver_no = (0 if (DOCTORS_NUMBER - 1 == no) else (no + 1))
			executor.submit(
				doctors[no].use_two_screwdrivers,
				screwdrivers[no],
				screwdrivers[left_screwdriver_no]
				)

