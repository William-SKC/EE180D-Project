import { NgModule, ErrorHandler } from '@angular/core';
import { IonicApp, IonicModule, IonicErrorHandler } from 'ionic-angular';
import { MyApp } from './app.component'

// import pages
import { HomePage } from '../pages/home/home';
import { NavPage } from '../pages/nav/nav';

// import providers
import { AngularFireModule } from 'angularfire2'

export const firebaseConfig = {
  // Initialize Firebase
    apiKey: "AIzaSyANX0Nglv7dJLRI0LPM28g_pAKfL7F5oFM",
    authDomain: "hospitably-c30d7.firebaseapp.com",
    databaseURL: "https://hospitably-c30d7.firebaseio.com",
    storageBucket: "hospitably-c30d7.appspot.com",
    messagingSenderId: "357236605341"  
};



@NgModule({
  declarations: [
    MyApp,
    HomePage,
    NavPage
  ],
  imports: [
    IonicModule.forRoot(MyApp),
      AngularFireModule.initializeApp(firebaseConfig)
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage,
    NavPage
  ],
  providers: [
  {provide: ErrorHandler, useClass: IonicErrorHandler},
  ]
})
export class AppModule {}
