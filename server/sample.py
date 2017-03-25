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
    position = ""
        #data_array[data]
    #data_list = data_string.split()
    #print type(data_list)
    # for y in range(0, 17):
    #     if data_array[0] <= 0.5 and data_array[1] <= 0.5 + y and data_array[1] > 0.5 + y - 1:
    #         position = "Position %s" % y
    # for x in range(0, 8):
    #     if data_array[0] <= .5 + x and data_array[0] > .5 + x - 1 and data_array[1] <= 16.9 and data_array > 15.9:
    #         position = "Position"

    if data_array[0] <= 0.5 and data_array[1] <= 0.5:
        position = "Position 0"
    elif data_array[0] <= 0.5 and data_array[1] <= 1.5 and data_array[1] > 0.5:
        position = "Position 1"
    elif data_array[0] <= 0.5 and data_array[1] <= 2.5 and data_array[1] > 1.5:
        position = "Position 2"
    elif data_array[0] <= 0.5 and data_array[1] <= 3.5 and data_array[1] > 2.5:
        position = "Position 3"
    elif data_array[0] <= 0.5 and data_array[1] <= 4.5 and data_array[1] > 3.5:
        position = "Position 4"
    elif data_array[0] <= 0.5 and data_array[1] <= 5.5 and data_array[1] > 4.5:
        position = "Position 5"
    elif data_array[0] <= 0.5 and data_array[1] <= 6.5 and data_array[1] > 5.5:
        position = "Position 6"
    elif data_array[0] <= 0.5 and data_array[1] <= 7.5 and data_array[1] > 6.5:
        position = "Position 7"
    elif data_array[0] <= 0.5 and data_array[1] <= 8.5 and data_array[1] > 7.5:
        position = "Position 8"
    elif data_array[0] <= 0.5 and data_array[1] <= 9.5 and data_array[1] > 8.5:
        position = "Position 9"
    elif data_array[0] <= 0.5 and data_array[1] <= 10.5 and data_array[1] > 9.5:
        position = "Position 10"
    elif data_array[0] <= 0.5 and data_array[1] <= 11.5 and data_array[1] > 10.5:
        position = "Position 11"
    elif data_array[0] <= 0.5 and data_array[1] <= 12.5 and data_array[1] > 11.5:
        position = "Position 12"
    elif data_array[0] <= 0.5 and data_array[1] <= 13.5 and data_array[1] > 12.5:
        position = "Position 13"
    elif data_array[0] <= 0.5 and data_array[1] <= 14.5 and data_array[1] > 13.5:
        position = "Position 14"
    elif data_array[0] <= 0.5 and data_array[1] <= 15.5 and data_array[1] > 14.5:
        position = "Position 15"
    elif data_array[0] <= 0.5 and data_array[1] <= 16.5 and data_array[1] > 15.5:
        position = "Position 16"
    elif data_array[0] <= 0.5 and data_array[1] <= 17.5 and data_array[1] > 16.5:
        position = "Position 17"
    elif data_array[0] <= 1.5 and data_array[0] > 0.5 and data_array[1] <= 16.9:
        position = "Position 18"
    elif data_array[0] <= 2.5 and data_array[0] > 1.5 and data_array[1] <= 16.9:
        position = "Position 19"
    elif data_array[0] <= 3.5 and data_array[0] > 2.5 and data_array[1] <= 16.9:
        position = "Position 20"
    elif data_array[0] <= 4.5 and data_array[0] > 3.5 and data_array[1] <= 16.9:
        position = "Position 21"
    elif data_array[0] <= 5.5 and data_array[0] > 4.5 and data_array[1] <= 16.9:
        position = "Position 22"
    elif data_array[0] <= 6.5 and data_array[0] > 5.5 and data_array[1] <= 16.9:
        position = "Position 23"
    elif data_array[0] <= 7.5 and data_array[0] > 6.5 and data_array[1] <= 16.9:
        position = "Position 24"
    elif data_array[0] <= 8.5 and data_array[0] > 7.5 and data_array[1] <= 16.9 and data_array[1] > 15.9:
        position = "Position 25"
    elif data_array[0] <= 8.5 and data_array[0] > 7.5 and data_array[1] <= 15.9 and data_array[1] > 14.9:
        position = "Position 26"
    elif data_array[0] <= 8.5 and data_array[0] > 7.5 and data_array[1] <= 14.9 and data_array[1] > 13.9:
        position = "Position 27"
    elif data_array[0] <= 8.5 and data_array[0] > 7.5 and data_array[1] <= 13.9 and data_array[1] > 12.9:
        position = "Position 28"
    elif data_array[0] <= 8.5 and data_array[0] > 7.5 and data_array[1] <= 12.9 and data_array[1] > 11.9:
        position = "Position 29"
    elif data_array[0] <= 8.5 and data_array[0] > 7.5 and data_array[1] <= 11.9 and data_array[1] > 10.9:
        position = "Position 30"
    elif data_array[0] <= 8.5 and data_array[0] > 7.5 and data_array[1] <= 10.9 and data_array[1] > 9.9:
        position = "Position 31"
    elif data_array[0] <= 8.5 and data_array[0] > 7.5 and data_array[1] <= 9.9 and data_array[1] > 8.9:
        position = "Position 32"
    elif data_array[0] <= 8.5 and data_array[0] > 7.5 and data_array[1] <= 8.9 and data_array[1] > 7.9:                                                                                                                                                                                                                                        
        position = "Position 33"
    elif data_array[0] <= 8.5 and data_array[0] > 7.5 and data_array[1] <= 7.9 and data_array[1] > 6.9:
        position = "Position 34"
    elif data_array[0] <= 8.5 and data_array[0] > 7.5 and data_array[1] <= 6.9 and data_array[1] > 5.9:
        position = "Position 35"
    elif data_array[0] <= 9.5 and data_array[0] > 8.5 and data_array[1] <= 6.5 and data_array[1] > 5.5:
        position = "Position 36"
    elif data_array[0] <= 10.5 and data_array[0] > 9.5 and data_array[1] <= 6.5 and data_array[1] > 5.5:
        position = "Position 37"
    elif data_array[0] <= 11.5 and data_array[0] > 10.5 and data_array[1] <= 6.5 and data_array[1] > 5.5:
        position = "Position 38"
    elif data_array[0] <= 12.5 and data_array[0] > 11.5 and data_array[1] <= 6.5 and data_array[1] > 5.5:
        position = "Position 39"
    elif data_array[0] <= 13.5 and data_array[0] > 12.5 and data_array[1] <= 6.5 and data_array[1] > 5.5:
        position = "Position 40"
    elif data_array[0] <= 14.5 and data_array[0] > 13.5 and data_array[1] <= 6.5 and data_array[1] > 5.5:
        position = "Position 41"
    elif data_array[0] <= 14.3 and data_array[0] > 13.3 and data_array[1] <= 5.5 and data_array[1] > 4.5:
        position = "Position 42"
    elif data_array[0] <= 14.3 and data_array[0] > 13.3 and data_array[1] <= 4.5 and data_array[1] > 3.5:
        position = "Position 43"
    elif data_array[0] <= 14.3 and data_array[0] > 13.3 and data_array[1] <= 3.5 and data_array[1] > 2.5:
        position = "Position 44"
    elif data_array[0] <= 14.3 and data_array[0] > 13.3 and data_array[1] <= 2.5 and data_array[1] > 1.5:
        position = "Position 45"
    elif data_array[0] <= 14.3 and data_array[0] > 13.3 and data_array[1] <= 1.5 and data_array[1] > 0.5:
        position = "Position 46"
    elif data_array[0] <= 14.3 and data_array[0] > 13.3 and data_array[1] <= 0.5:
        position = "Position 47"
    elif data_array[0] <= 13.3 and data_array[0] > 12.3 and data_array[1] <= 0.5:
        position = "Position 48"
    elif data_array[0] <= 12.3 and data_array[0] > 11.3 and data_array[1] <= 0.5:
        position = "Position 49"
    elif data_array[0] <= 11.3 and data_array[0] > 10.3 and data_array[1] <= 0.5:
        position = "Position 50"
    elif data_array[0] <= 10.3 and data_array[0] > 9.3 and data_array[1] <= 0.5:
        position = "Position 51"
    elif data_array[0] <= 9.3 and data_array[0] > 8.3 and data_array[1] <= 0.5:
        position = "Position 52"
    elif data_array[0] <= 8.3 and data_array[0] > 7.3 and data_array[1] <= 0.5:
        position = "Position 53"
    elif data_array[0] <= 7.3 and data_array[0] > 6.3 and data_array[1] <= 0.5:
        position = "Position 54"
    elif data_array[0] <= 6.3 and data_array[0] > 5.3 and data_array[1] <= 0.5:
        position = "Position 55"
    elif data_array[0] <= 5.3 and data_array[0] > 4.3 and data_array[1] <= 0.5:
        position = "Position 56"
    elif data_array[0] <= 4.3 and data_array[0] > 3.3 and data_array[1] <= 0.5:
        position = "Position 57"
    elif data_array[0] <= 3.3 and data_array[0] > 2.3 and data_array[1] <= 0.5:
        position = "Position 58"
    elif data_array[0] <= 2.3 and data_array[0] > 1.3 and data_array[1] <= 0.5:
        position = "Position 59"
    elif data_array[0] <= 1.3 and data_array[0] > 0.3 and data_array[1] <= 0.5:
        position = "Position 60"
    

    

    #result = firebase.post('loc_data', {'position':position})
    result = firebase.post('loc_data', {'time':data_array[0], 'dx':data_array[1], 'dy':data_array[2]})
    #print data_list[0]
    #print data_list[1]
    #print data_list[2]

#streamData([14, 1, 1])

# Add listener to colors child with no callback
#no_callback = fb.child("Users").listener()

# Or use a custom callback
#custom_callback = fb.child("Users").listener(p)

# Start and stop the stream using the following
#custom_callback.start()
#raw_input("ENTER to stop...")
#custom_callback.stop()
