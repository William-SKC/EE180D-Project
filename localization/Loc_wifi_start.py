
import numpy as np
import scipy.stats
import time 

import loc_point_class

def Loc_wifi_start(map_dict,list_dict_point):
    start_time = time.time()
    print('start: %s' %start_time )
    with open("scan_results.txt") as scan_file:
        dic_scan = dict(line.split() for line in scan_file)

    status_file = open('status.txt', 'w')

    loc_point_list = []
    i = 0
    while i < len(list_dict_point):
        point_dict = list_dict_point[i]
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
        
        [x_loc, y_loc] = map_dict[str(i)]
        x = loc_point_class.loc_point(i, float(x_loc), float(y_loc), prob)
        loc_point_list.append(x)
        
        if prob < 0.1 and i <= 56:
            i = i + 4
        else:
            i = i + 1	
    
        print('go through all the point: %s' %(time.time() - start_time))
    
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
        print ('current location: ' + 'x=' + str(x_est) + '\t'+ 'y='+str(y_est))

        open('history.txt', 'w').close()
        with open('history.txt', 'w') as f:
            f.write(str(strength_list[0].name) + '\t' + str(x_est) + '\t'+ str(y_est) + '\n')


        status_file.write(str(strength_list[0].name) + '\t' + str(x_est) + '\t'+ str(y_est))
        status_file.close
        print('done: %s' %(time.time() - start_time))
        return 1


    else: 
        print ('Not in the area')
        return 0 
    
