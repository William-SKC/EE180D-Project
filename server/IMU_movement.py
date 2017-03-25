import time
import os
import sys
import math

def IMU_movement(rec_data, direction, stride): 
	# rec_data[0] is turns: 0 -> no turn, 1 ->right, -1 ->left
	# rec_data[1] is # of steps taken
	#movement[0]: time 
	# movements[1] = change on x-axis
	# movements[2] = change on y-axis	
	turn = rec_data[0]
	num_steps = rec_data[1]
	movements = [0, 0, 0]
	movements[0] = time.time()
	dX = 0
	dY = 0

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
	elif direction == 'S':
	    dY = -stride*num_steps
	elif direction == 'E':
	    dX = stride*num_steps
	elif direction == 'W':
	    dX = -stride*num_steps

	movements[1] = dX
	movements[2] = dY
	return [movements, direction] 
