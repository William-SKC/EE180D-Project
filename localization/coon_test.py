import numpy as np
import scipy.stats
import os
import sys
import server


conn = server.server_ini()

while 1:
		msg = server.server_cont(conn)
		print 'msg: '
		print msg
