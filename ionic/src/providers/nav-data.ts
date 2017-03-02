import { Injectable } from '@angular/core';
import 'rxjs/add/operator/map';


/*
  Generated class for the NavData provider.

  See https://angular.io/docs/ts/latest/guide/dependency-injection.html
  for more info on providers and Angular 2 DI.
*/
@Injectable()
export class NavData {
	// We'll use this to create a database reference to the user profile
	userCoord: any;

	// We'll use this to create an auth reference to the logged in user
	currentUser: any;


  constructor()  {
  	this.currentUser = firebase.auth().currentUser;
  	this.userCoord = firebase.database().ref('/User')
  }

  getUserCoord(): any {
  	return this.userCoord.child(this.currentUser.Location);
  }

}


var position = firebase.database().ref('Users/Toggle');
position.equalTo("true")


