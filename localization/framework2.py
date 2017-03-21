## EE180DB Localization w/ only wifi strengths
import numpy as np
import scipy.stats
import os
import sys
import server
import time


import Loc_wifi_ini
import wifi_localization_once
import localization_adjustment
import sample
import IMU_movement

from threading import Thread
from multiprocessing import Process, Array, Lock, Manager, Value
from functools import partial

def localization_wifi(curr_state, lock, hist_loc, map_dict, list_dict_point):
	try:

		while 1:
			scan_states = wifi_localization_once.wifi_localization_once(map_dict, list_dict_point) # return [x, y, time]
			print('Wifi scan: '+ str(scan_states[0]) + ' ' + str(scan_states[1]) + ' ' + str(scan_states[2]))
			#time.sleep(2)

			#adjustment
		#	localization_adjustment.localization_adjustment(curr_state, lock, hist_loc, scan_states)
			#time.sleep(1)


	except KeyboardInterrupt:
		print 'interrupted and stopped!'

def localization_IMU(curr_state, lock, hist_loc, conn):
	while 1:
		msg = server.server_cont(conn)
		print 'msg:'
		print msg
		rec_data = [int(msg.split( )[0]), int(msg.split( )[1])]
		print 'received data:'
		print rec_data
		# interpret the received data
		movements = IMU_movement.IMU_movement(rec_data, direction)

		with lock:
			curr_state[0] = movements[0]
			curr_state[1] = curr_state[1]+movements[1]
			curr_state[2] = curr_state[2]+movements[2]
			hist_loc[str(curr_state[0])] = curr_state[1:]
			print('******	Current	states	******')
			print('IMU: '+ str(curr_state[0]) + ' ' + str(curr_state[1]) + ' ' + str(curr_state[2]))
			print('********************************\n')
		#time.sleep(0.5)
                with lock:
                        sample.streamData(curr_state)

#### main: 
print('Welcome to Localization\n')
#Initialization
[map_dict,list_dict_point] = Loc_wifi_ini.Loc_wifi_ini()
conn = server.server_ini()
os.system('chmod +x testPoint.sh')

# create shared variables
test_val = Value('f',0)
lock = Lock()
hist_loc = Manager().dict()

user_height = raw_input('Please enter your height: ')
direction = raw_input('Please enter your facing direction: ')
stride = ((height * .413)/120)*2

starting_loc = wifi_localization_once.wifi_localization_once(map_dict, list_dict_point)
while starting_loc == 0:
   	starting_loc = wifi_localization_once.wifi_localization_once(map_dict, list_dict_point)
    print("rescaned from starting location.")
print 'starting loc: '
print starting_loc
curr_state = Array('d', starting_loc)


p_wifi = partial(localization_wifi, curr_state, lock, hist_loc, map_dict, list_dict_point)
p_IMU = partial(localization_IMU, curr_state, lock, hist_loc, conn)

pro_wifi = Process(name = 'pro_wifi', target=p_wifi)
pro_IMU = Process(name='pro_IMU', target=p_IMU)


# processes start
pro_wifi.start()
pro_IMU.start()

pro_wifi.join()
pro_IMU.join()






