#!/usr/bin/python

from RPIO import PWM
import sys
import time


class PapaFeederCtrl:
	"""Class to control Feeder from PaPasPy
	Uses RPi.GPIO """
	def __init__(self):
		self.gpio = 18
		self.pulse_open = 500
		self.pulse_close = 2000
		self.servo = PWM.Servo() 
	
	
	def open(self):
		self.move(self.pulse_open)		

	def close(self):
		self.move(self.pulse_close)	

	def move(self,pulse):
		self.servo.set_servo(self.gpio,pulse)
		#self.servo.stop_servo(self.gpio)


if __name__ == '__main__':
	if len(sys.argv) > 1:
		c = PapaFeederCtrl()
		if sys.argv[1] == 'open':
			c.open()
		else:
			c.close()
	else:
		print 'Usage: PapaFeederCtrl open|close'
		


