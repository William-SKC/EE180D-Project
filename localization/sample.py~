from firebase_streaming import Firebase
from firebase import firebase


# Sample callback function
#def p(x):
    #print x

# Firebase object
firebase = firebase.FirebaseApplication('https://hospitably-c30d7.firebaseio.com/')
fb = Firebase('https://hospitably-c30d7.firebaseio.com/')

def streamData(data_array):
    #for data in data_array:
        
        #data_array[data]
    #data_list = data_string.split()
    #print type(data_list)
    result = firebase.post('loc_data', {'time':data_array[0], 'dx':data_array[1], 'dy':data_array[2]})
    #print data_list[0]
    #print data_list[1]
    #print data_list[2]

streamData([1, 1, 1])

# Add listener to colors child with no callback
#no_callback = fb.child("Users").listener()

# Or use a custom callback
#custom_callback = fb.child("Users").listener(p)

# Start and stop the stream using the following
#custom_callback.start()
#raw_input("ENTER to stop...")
#custom_callback.stop()
