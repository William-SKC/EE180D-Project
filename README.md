

#UCLA EE180D-Project: Hospitably

## Creators:
Gary Bui, Shengkang "William" Chen, Victor Hsiang, Arad Saebi

## Synopsis
Hospitably is a web application that is designed to create an automated hospital experience. The focus of our project was within the scope of navigation by utilizing WiFi address and signal strength mapping. Furthermore, we used an IMU to enrich our navigation algorithm, as it provides data from which we can determine the distance a user travels. The combination of WiFi localization and IMU tracking gives an accurate representation of where the user is standing while they are indoors. Outside the context of hospitals, our project has the potential to track or localize inside any building with WiFi connectivity. As long as the reference data points are mapped out, it is simple to switch out the map in the cloud database and run an indoor localization system anywhere.

The navigation is based on Kalman Filter which takes into account of both measurement and propagation. In our case, we use the Intel Edison to Wifi scan and collect reference data and motion sensing using 9DOF mounted on shoes to collect propagation data. Using a probabilistic method, we are able to compare a user’s WiFi scan to our reference map, hosted on the Firebase Database, to determine location. Meanwhile, 9DOF can identify user’s footsteps and turns to estimate user’s change in location.

There are three main parts of this project: server, client and database. Server will be a Intel Edison Board which will handle the WiFi scan, localization calculation and communicate with database. Server will be a Intel Edison Board mounted on a 9DOF which will handle the motion sensing. The database we use is Firebase which store all the reference maps. 



## To clone
##<pre><code>git clone git@github.com:William-SKC/EE180D-Project.git</code></pre>
##If you want to work on a part of the code, create a new branch:
* <pre><code>git branch \<branch name\></code></pre>
* When you are done with your code, then you can merge it back into master.
* To do this, go to the git repository and submit a merge request.
* Your team members will check your work and merge the code.


## To start up Ionic application
### Refer to [this Ionic tutorial](https://scotch.io/tutorials/build-a-mobile-app-with-angular-2-and-ionic-2).
* Install Cordova
* <pre><code>npm install -g cordova</code></pre>
* Install Ionic CLI
* <pre><code>npm install -g ionic</code></pre>
* Install Typescript \(This is the language Ionic is written in. It is similar to JS\)
* <pre><code>npm install -g typescript</code></pre>
* Start up the app! Use command -l to see all OS emulations.
* <pre><code>ionic serve</code></pre>


## To run the program
* Locations for the folders
*Put the server folder into Intel Edison board for WiFI scanning, put the client folder in the Intel Edison Board mounted on a 9DOF.
* Go to the  server folder
* cd server
* Run the server framework
* python framework.py
* Enter the informations needed on the terminals 
* Wait for it until it shows “Listening to the client...”
* Go to the client  folder
* cd client
* Run the motion sensing on the 9DOF
* python motion_sensing.py

## Descriptions of folders and files 
* framework.py
* The main program on the server’s side. It handles the WiFi scan, localization calculation and communicate with database
* IMU_movement.py
* Translate steps and turns to movements on x-axis and y-axis given direction
* loc_point_ class.py
* It is a class to store information for each reference point for sorting in WiFi scan localization
* localization_adjustment
*Calculate a better estimated location using two estimated locations from motion sensing and WiFi scan based on Kalman gain
* map_drawing.py
*Matches each reference point with its x,y coordinates 
* testPoint.sh
* Shell script for WiFi scan
* wifi_localization_once
* Localization using WiFi scan only
* motion_sensing.py
* Create client connection
*Detects the number of steps and turns

##Database
We are using Firebase as our database
