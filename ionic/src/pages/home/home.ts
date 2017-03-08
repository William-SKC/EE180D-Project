import { Component } from '@angular/core';

import { NavController, AlertController } from 'ionic-angular';

import { AngularFire, FirebaseListObservable} from 'angularfire2'

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  users: FirebaseListObservable<any>
  loc: FirebaseListObservable<any>

  constructor(public navCtrl: NavController, public alertCtrl: AlertController, angFire: AngularFire) {
  	//Declares angFire objects on the class HomePage and directs them to their specific node.
  	this.users = angFire.database.list('/Users');
  	this.loc = angFire.database.list('/Users/Locations')
  }

  //This is a function that provides the logic for the button for adding users.
  addUser():void {
    //Create an object that is an alertCtrl with the following title, message, and inputs
  	let prompt = this.alertCtrl.create({
  		title: 'Welcome to Hospitably',
  		message: 'Enter your name and position',
  		inputs: [
  		{
  			name: 'user',
  			placeholder: 'Your Name"'
  		},
  		{
  			name: 'dest',
  			placeholder: 'Where do you want to go?'
  		}
  	],
  	buttons: [
  		{
  			text: "Cancel",
  			handler: data => {
  				console.log("cancel clicked");
  			}
  		},
  		{
        //When the navigate button is pressed, push the inputs into the angFire object that is linked to a node
        //Need to know when navigate is pressed, then need to call the command to calculate the current position
        //I can't call python in TS, so my options are to trigger the python script through the firebase by having an observer in node.js to watch 
        //for a new user and to call the python script when this happens. I can also just write everything in js through node.js but i think it'd be 
        //easier to just do the first option
  			text: "Navigate",
  			handler: data => {
  				this.users.push({
  					Name: data.user,
  					Destination: data.dest,
  					Toggle: "on"
  				})
  			}
  		}
  	]
  	});
  	prompt.present();
  }

}
