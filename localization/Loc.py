## EE180DB Localization w/ only wifi strengths
import numpy as np
import scipy.stats
import os
import sys

os.system(command)
import Loc_wifi_ini
import Loc_wifi_start
import Loc_wifi_cont

print('Welcome to Localization w/ only wifi strengths\n')
[map_dict,list_dict_point] = Loc_wifi_ini.Loc_wifi_ini()



os.system('chmod +x filename.sh')


while 1:
	control_signal = raw_input('Operation ([s]-start, [c]-continue, [q]-quit): ')
	pass
	if control_signal == 's':
		os.system('sh testPoint.sh')
		Loc_wifi_start.Loc_wifi_start(map_dict,list_dict_point)
	elif control_signal == 'c':
		Loc_wifi_cont.Loc_wifi_cont(map_dict,list_dict_point)
	elif control_signal == 'q':
		print ("Exit localization")
		break
	else:
		print("option invalid")