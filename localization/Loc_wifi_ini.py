## EE180DB Localization w/ only wifi strengths
import numpy as np
import scipy.stats
import os
import json

import loc_point_class

#Reads the reference point coordinates from a text file and loads them into a dictionary
def Loc_wifi_ini():
    map_dict = {}
    with open('points_map.txt', 'r') as point_map:
        for line in point_map:
            splitLine = line.split()
            map_dict.update({line.split()[0]: [line.split()[1], line.split()[2]]})

    #list of dictionaries   
    list_dict_point = []

    #Reads the reference point information into a list of dictionaries, one dictionary per reference point
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

    #makes a json tree of the reference points
    #with open('result.json', 'w') as fp:
        #json.dump(list_dict_point, fp)


    return [map_dict,list_dict_point] 