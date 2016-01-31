#!/usr/bin/python

import subprocess
import sys

class PapaTwitterCtrl:
	"""Class so send twitter from PaPasPy
	It uses CLI privided by  http://mike.verdone.ca/twitter/"""

	def tweet(self,msg):
		cmd = "twitter set " + msg
		# os.system(cmd)
		proc = subprocess.Popen(cmd, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		c = PapaTwitterCtrl()
		c.tweet(sys.argv[1])
	else:
		print 'Usage: PapaTwitterCtrl "Your message"'
		


