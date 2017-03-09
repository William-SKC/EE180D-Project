from itertools import izip
import json
from firebase import firebase
firebase = firebase.FirebaseApplication('https://hospitably-c30d7.firebaseio.com/', None)
result = firebase.get('/map', None)
json1_data = result[0]
json2_data = result[1]
#print type(json1_data)
#print json1_data
print json2_data
#print result
 
