## EE180DB Localization w/ only wifi strengths
import numpy as np
import scipy.stats
import os

import Loc_wifi_ini
import Loc_wifi_start
import Loc_wifi_cont

print('Welcome to Localization w/ only wifi strengths\n')
#Have the user enter a command
control_signal = raw_input('Operation ([s]-start, [c]-continue, [q]-quit): ')

#Initialize a map dictionary and a reference point dictionary
[map_dict,list_dict_point] = Loc_wifi_ini.Loc_wifi_ini()

while 1:
	pass
	#if user chooses start, use starting code
	if control_signal == 's':
		Loc_wifi_start.Loc_wifi_start(map_dict,list_dict_point)
		break
	#if user chooses continue, use continuing code
	elif control_signal == 'c':
		Loc_wifi_cont.Loc_wifi_cont(map_dict,list_dict_point)
		break
	#if user chooses quit, quit
	elif control_signal == 'q':
		print ("Exit localization")
		break
	else:
		print("option invalid")