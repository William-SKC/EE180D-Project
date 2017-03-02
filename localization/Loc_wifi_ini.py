## EE180DB Localization w/ only wifi strengths
import numpy as np
import scipy.stats
import os

import loc_point_class

def Loc_wifi_ini():
    map_dict = {}
    with open('points_map.txt', 'r') as point_map:
        for line in point_map:
            splitLine = line.split()
            map_dict.update({line.split()[0]: [line.split()[1], line.split()[2]]})

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

    point_map.close()

    return [map_dict,list_dict_point] 