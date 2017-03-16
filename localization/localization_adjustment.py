import numpy as np


def get_nearest_less_element(d, k):
    return d[str(max(key for key in map(float, d.keys()) if key <= k))]


def localization_adjustment(curr_state, lock, hist_loc, scan_states):
	print 'scan_states: '
	print scan_states
	scan_time = scan_states[0]
	scan_time = scan_time+0.5 # add uncertainties
	print('Adjust current states: '+ str(curr_state[0]) + ' ' + str(curr_state[1]) + ' ' + str(curr_state[2]) + '\n')	
	print hist_loc
	print scan_time
	with lock:
		num = scan_time
		matched_loc = hist_loc.get(num, hist_loc[min(hist_loc.keys(), key=lambda k: abs(float(k)-num))]) # find the clostest key(time) for matched location
	print 'matched loc'
	print matched_loc

	#calculate kalman_gain (how much do we trust the adjustment and wifi localization)
	kalman_gain = 0.6

	#adjust current location based on scan_wifi(before)
	adjust_amount = np.subtract(matched_loc, scan_states[1:])
	print 'adjust_amount: '
	print adjust_amount
	print('before adjustment for current states: '+ str(curr_state[0]) + ' ' + str(curr_state[1]) + ' ' + str(curr_state[2]) + '\n')
	with lock:
		curr_state[1] = curr_state[1]+adjust_amount[0]*kalman_gain
		curr_state[2] = curr_state[2]+adjust_amount[1]*kalman_gain
	print('after adjustment for current states: '+ str(curr_state[0]) + ' ' + str(curr_state[1]) + ' ' + str(curr_state[2]) + '\n')
	print matched_loc


	pass
