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
  	var ref = firebase.database.ref("Users");
  	// ref.child("Users").orderByChild("Toggle").equalTo("on").once("value",function(snapshot) {
    // var userData = snapshot.val();
    // if (userData){
    //   console.log("exists!");
    // }
// });

  	this.users = angFire.database.list('/Users');
  	this.loc = angFire.database.list('/Users/Locations');

  	// this.users.subscribe(
  	// 	scan => this.loc.push({
  	// 		Location: "Position 1"
  	// 	})
  	// 	);
  }

  addUser():void {
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
