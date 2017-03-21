import time
import os
import sys
import math

def IMU_movement(rec_data, direction): 
	# rec_data[0] is turns: 0 -> no turn, 1 ->right, -1 ->left
	# rec_data[1] is # of steps taken
#movement[0]: time 
# movement[1] = change on x-axis
# movement[2] = change on y-axis	
turn = rec_data[0]
num_steps = rec_data[1]
movement = [0, 0, 0]
movement[0] = time.time()


#determine location
if direction == 'N' and turn == 1: 
    direction = 'E'
elif direction == 'N' and turn == -1:
    direction = 'W'
elif direction == 'E' and turn == 1:
    direction = 'S'
elif direction == 'E' and turn == -1:
    direction = 'N'
elif direction == 'S' and turn == 1:
    direction = 'W'
elif direction == 'S' and turn == -1:
    direction = 'E'
elif direction == 'W' and turn == 1:
    direction = 'N' 
elif direction == 'W' and turn == -1:
    direction = 'S'

if direction == 'N':
    dY = stride*num_steps
if direction == 'S':
    dY = -stride*num_steps
if direction == 'E':
    dX = stride*num_steps
if direction == 'W':
    dX = -stride*num_steps


return movements