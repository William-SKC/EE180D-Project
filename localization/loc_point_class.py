## EE180DB Localization w/ only wifi strengths
import numpy as np
#A loc_point initializes with a name, an x location, and a y location
class loc_point:
    
    def __init__(self,name, x_loc, y_loc, prob):
        self.name = name
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.prob = prob

    #updates the probablity of a location point
    def update_prob(self, prob):
        self.prob = prob

    #display the name of the location and their probability
    def display_loc(self):
         print "Name : ", self.name,  ", probability: ", self.prob
