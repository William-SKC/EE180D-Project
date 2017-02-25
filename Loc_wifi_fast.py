## EE180DB Localization w/ only wifi strengths
import numpy as np
import scipy.stats
import os

class loc_point:
    
    def __init__(self,name, x_loc, y_loc):
        self.name = name
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.prob = 0

    def update_prob(self, prob):
        self.prob = prob

    def display_loc(self):
         print "Name : ", self.name,  ", probability: ", self.prob


point_map = open('points_map.txt', 'r')

with open("scan_results.txt") as scan_file:
        dic_scan=dict(line.split() for line in scan_file)

loc_point_list = []  
list_dict_point = []




for i in range (0, 61):
    file_name = 'FINAL_%d.txt' %i
    file="/reference_points/"+file_name
    path=os.getcwd()+file

    point_dict = {}

    with open(path, 'r') as f:
        for line in f:
            splitLine = line.split()
            point_dict.update({line.split()[0]: [line.split()[1], line.split()[2]]})
    list_dict_point.append(point_dict)

    line_map = point_map.readline()
    [x_loc, y_loc] = [float(line_map.split()[1]), float(line_map.split()[2])] 
    x = loc_point(i, x_loc, y_loc)
    loc_point_list.append(x)

for i, point_dict in enumerate(list_dict_point):
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
    loc_point_list[i].update_prob(prob)

    strength_list = sorted(loc_point_list, key=lambda loc: loc.prob, reverse=True)


for j in range (len(strength_list)):
    print "Name : ", strength_list[j].name, ", probability: ", strength_list[j].prob

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
    print ('estimate location: ' + 'x=' + str(x_est) + '\t'+ 'y='+str(y_est))
else: 
    print ('Not in the area')



point_map.close()


