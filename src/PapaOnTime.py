#!/usr/bin/python

import time
import sys
from api import PapaSoundCtrl, PapaTwitterCtrl


class PapaOnTime:

	def __init__(self):
		self.twitter = PapaTwitterCtrl.PapaTwitterCtrl()
		self.sound = PapaSoundCtrl.PapaSoundCtrl()
	
	def tweet(self,msg):
		self.twitter.tweet(str(msg))

	def play(self,tune):
		self.sound.play(str(tune))

if __name__ == '__main__':
	if len(sys.argv) > 3:

		minutes = int(sys.argv[1])
		seconds = minutes * 60
		tune = str(sys.argv[2])
		message = str(sys.argv[3])
		
		papa = PapaOnTime()
		
				
		print time.ctime(), " PapaOnTime started"
		print time.ctime(), " Press Ctr+C to exit" 
		
		print time.ctime(), " I'm going to run every ", minutes , " minutes"
		
		while True:
			print time.ctime(), " Sleeping for ", minutes , " minutes" 
			time.sleep(seconds)
			print time.ctime(), " Wake-up!"
			papa.tweet(time.ctime() + ' Playing sound')
			papa.play(tune)
	else:
		print "Usage: PapaOnline minutes path_to_tune.mp3 'Message to twitter'"
