from firebase_streaming import Firebase

# Sample callback function
def p(x):
    print x

# Firebase object
fb = Firebase('https://hospitably-c30d7.firebaseio.com/')

# Add listener to colors child with no callback
#no_callback = fb.child("Users").listener()

# Or use a custom callback
custom_callback = fb.child("Users").listener(p)

# Start and stop the stream using the following
custom_callback.start()
raw_input("ENTER to stop...")
custom_callback.stop()
