#!/usr/bin/python

import subprocess
import sys

class PapaSoundCtrl:
	"""Class to play mp3 from PaPasPy
	It uses CLI privided by http://mpg321.sourceforge.net/"""

	def play(self,tune):
		cmd = "mpg321 -g 100 -q " + tune
		proc = subprocess.Popen(cmd, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)		

if __name__ == '__main__':
	if len(sys.argv) > 1:
		c = PapaSoundCtrl()
		c.play(sys.argv[1])
	else:
		print 'Usage: PapaSoundCtrl your_tune.mp3'
		


