#!/usr/bin/python

import time
import sys

sys.path.append('/home/pi/papaspy/lib/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCD')
from Adafruit_CharLCD import Adafruit_CharLCD

class PapaDisplayCtrl:
	"""Class to display text from PaPasPy
	"""
	def __init__(self):
		self.lcd = Adafruit_CharLCD()
		self.lcd.begin(16,1)
		self.lcd.clear()

	def display(self, msg):
		self.lcd.clear()
		self.lcd.message(msg)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		c = PapaDisplayCtrl()
		c.display(sys.argv[1])
	else:
		print 'Usage: PapaDisplayCtrl message'
		


