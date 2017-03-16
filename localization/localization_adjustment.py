import numpy as np
import math

def get_nearest_less_element(d, k):
    return d[str(max(key for key in map(float, d.keys()) if key <= k))]


def localization_adjustment(curr_state, lock, hist_loc, scan_states):
	print 'scan_states: '
	print scan_states
	scan_time = scan_states[0]
	print('Adjust current states: '+ str(curr_state[0]) + ' ' + str(curr_state[1]) + ' ' + str(curr_state[2]))	
	print hist_loc
	print scan_time
	with lock:
		num = scan_time
		matched_loc = hist_loc.get(num, hist_loc[min(hist_loc.keys(), key=lambda k: abs(float(k)-num))]) # find the clostest key(time) for matched location
	print 'matched loc'
	print matched_loc

	#calculate kalman_gain (how much do we trust the adjustment and wifi localization)
	kalman_gain = 0.6
	with lock:
		temp_time = curr_state[0]
		temp_x = curr_state[1]
		temp_y = curr_state[2]
	rate_change = math.sqrt(math.pow((scan_states[1]-temp_x),2)+math.pow((scan_states[2]-temp_y),2)/math.pow((temp_time - scan_states[0]),2))
	print rate_change
	kalman_gain = math.exp(-1*rate_change/16)
	print 'kalman_gain'
	print kalman_gain

	#adjust current location based on scan_wifi(before)
	adjust_amount = np.subtract(matched_loc, scan_states[1:])
	print 'adjust_amount: '
	print adjust_amount
	print('before adjustment for current states: '+ str(curr_state[0]) + ' ' + str(curr_state[1]) + ' ' + str(curr_state[2]))
	with lock:
		curr_state[1] = curr_state[1]+adjust_amount[0]*kalman_gain
		curr_state[2] = curr_state[2]+adjust_amount[1]*kalman_gain
	print('after adjustment for current states: '+ str(curr_state[0]) + ' ' + str(curr_state[1]) + ' ' + str(curr_state[2]))
	print matched_loc


	pass
