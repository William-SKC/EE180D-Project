import numpy as np




points_map = open("points_map.txt",'w')
x = 0.5
y = 0.5
for i in range (0,61):
	if i <=  17:
		points_map.write(str(i) + '\t'+str(x) + ' \t' +str(y) + '\n')
		y = y + 1
	elif i > 17 and i <= 25:
		y = 16.9
		x = x + 1
		points_map.write(str(i) + '\t'+str(x) + ' \t' +str(y) + '\n')
	elif i > 25 and i <= 35:
		y = y - 1
		points_map.write(str(i) + '\t'+str(x) + ' \t' +str(y) + '\n')	
	elif i == 36: 
		y = 6.5
		x = 9.5
		points_map.write(str(i) + '\t'+str(x) + ' \t' +str(y) + '\n')	

	elif i > 36 and i <= 41:
		x = x + 1
		points_map.write(str(i) + '\t'+str(x) + ' \t' +str(y) + '\n')	
	elif i > 41 and i <= 47:
		y = y - 1
		x = 14.3
		points_map.write(str(i) + '\t'+str(x) + ' \t' +str(y) + '\n')
	elif i > 47:
		x = x - 1
		points_map.write(str(i) + '\t'+str(x) + ' \t' +str(y) + '\n')
		


points_map.close()
