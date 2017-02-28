## EE180DB Localization w/ only wifi strengths
import numpy as np
class loc_point:
    
    def __init__(self,name, x_loc, y_loc, prob):
        self.name = name
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.prob = prob

    def update_prob(self, prob):
        self.prob = prob


    def display_loc(self):
         print "Name : ", self.name,  ", probability: ", self.prob
