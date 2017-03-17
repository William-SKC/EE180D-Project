## EE180DB Localization w/ only wifi strengths
import numpy as np
import scipy.stats
import os
import sys

import Loc_wifi_ini
import wifi_localization_once
import server
import time


from threading import Thread
from multiprocessing import Process, Array, Lock, Manager
from functools import partial


def add(lock, curr_loc):
	while 1:
		with lock:
			curr_loc[0] = curr_loc[0]+4
			print('Add: '+str(curr_loc[0]))
		time.sleep(0.3)

def sub(lock, curr_loc):
	while 1:
		with lock:
			curr_loc[0] = curr_loc[0]+5
			print('Sub: '+str(curr_loc[0]))
		time.sleep(3)

def localization_wifi(curr_loc, lock, map_dict, list_dict_point):
	try:
		while 1:
			curr_states = wifi_localization_once.wifi_localization_once(map_dict, list_dict_point) # return [x, y, time]
			print curr_states
			with lock:
				curr_loc = curr_states[:2]
				print curr_loc
				print curr_states[2]
				hist_loc[str(curr_states[2])] = curr_loc
		#	print hist_loc
		#	time.sleep(1)
	except KeyboardInterrupt:
		print 'interrupted and stopped!'

def localization_IMU(curr_loc, lock, conn):
	while 1:
		msg = server.server_cont(conn)
		with lock:
			#curr_loc = temp_loc
			print msg
			#try:
				#print('IMU Localization Updated: ' + str(curr_loc[0]) + ' ' + str(curr_loc[1]) +'\n')
		pass


print('Welcome to Localization\n')
#Initialization
[map_dict,list_dict_point] = Loc_wifi_ini.Loc_wifi_ini()
#conn = server.server_ini()
os.system('chmod +x testPoint.sh')

lock = Lock()
curr_loc = Array('d', [0,0])

hist_loc = Manager().dict()

p_wifi = partial(localization_wifi, curr_loc, lock, map_dict, list_dict_point)
#p_IMU = partial(localization_IMU, curr_loc, lock, conn)

p_add = partial(add, lock, curr_loc)
p_sub = partial(sub, lock, curr_loc)


pro_wifi = Process(name = 'pro_wifi', target=p_wifi)
#pro_IMU = Process(name='pro_IMU', target=p_IMU)
pro_sub = Process(name = 'pro_sub', target = p_sub)

pro_wifi.start()
#pro_IMU.start()
pro_sub.start()

pro_wifi.join()
pro_sub.join()





