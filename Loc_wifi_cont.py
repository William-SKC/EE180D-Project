## EE180DB Localization w/ only wifi strengths
import numpy as np
import scipy.stats

import loc_point_class

def Loc_wifi_cont(map_dict,list_dict_point):
	status_file = open('status.txt', 'r+') 

	s_status = status_file.readline()
	if(s_status):
		starting_point  = int(s_status.split( )[0])
		current_loc = [float(s_status.split( )[1]), float(s_status.split( )[2])]
	else:
		print("There is not starting position")
		return 0 

	with open("scan_results.txt") as scan_file:
            dic_scan=dict(line.split() for line in scan_file)

	loc_point_list = []  
	starting_point = starting_point-5
	for i in range (0, 10):
		check_pos = (i+starting_point)%61
		print check_pos
		point_dict = list_dict_point[check_pos]
		prob = 0
		for addr in point_dict:
			if addr in dic_scan:
					[pt_mean, pt_std] = point_dict[addr]
					scan_strength = dic_scan[addr]
					pt_mean = float(pt_mean)
					pt_std = float(pt_std)
					scan_strength = float(scan_strength)
					addr_prob = min(scipy.stats.norm(pt_mean, pt_std).cdf(scan_strength), 1 - scipy.stats.norm(pt_mean, pt_std).cdf(scan_strength))
					prob = prob + addr_prob

		[x_loc, y_loc] = map_dict[str(check_pos)]
		x = loc_point_class.loc_point(check_pos, float(x_loc), float(y_loc), prob)
		loc_point_list.append(x)


	strength_list = sorted(loc_point_list, key=lambda loc: loc.prob, reverse=True)

	for j in range (len(strength_list)):
		print "Name : ", loc_point_list[j].name, ", probability: ", loc_point_list[j].prob

	totsum = strength_list[0].prob
	x_acc = strength_list[0].x_loc * strength_list[0].prob
	y_acc = strength_list[0].y_loc * strength_list[0].prob

	for l in range (1, 5):
		if  strength_list[0].x_loc - 3 < strength_list[l].x_loc < strength_list[0].x_loc + 3 and strength_list[0].y_loc - 3 <strength_list[l].y_loc < strength_list[0].y_loc + 3:
			totsum = totsum + strength_list[l].prob
			x_acc = x_acc + strength_list[l].x_loc*strength_list[l].prob
			y_acc = y_acc + strength_list[l].y_loc*strength_list[l].prob
		else:
			break

	if totsum != 0:
		x_est = x_acc/totsum
		y_est = y_acc/totsum
		cloest_ref_point = strength_list[0].name

		content = status_file.read()	 #update the new location estimate 
		status_file.seek(0, 0)
		status_file.write(str(strength_list[0].name) + '\t' + str(x_est) + '\t'+ str(y_est))
		status_file.close

		with open('history.txt', 'r+') as f:
			line_f = f.readline()
			while(line_f):
				line_f = f.readline()
				pass
			f.write(str(strength_list[0].name) + '\t' + str(x_est) + '\t'+ str(y_est) + '\n')

		print ('Current location: ' + 'x=' + str(x_est) + '\t'+ 'y='+str(y_est))
		return 1

	else: 
		print ('Not in the area')
		return 0 



	
