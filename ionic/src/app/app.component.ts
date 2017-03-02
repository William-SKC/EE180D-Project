import { Component, ViewChild } from '@angular/core';
import { Platform, MenuController, Nav } from 'ionic-angular';
import { StatusBar, Splashscreen } from 'ionic-native';

import { HomePage } from '../pages/home/home';
import { NavPage } from '../pages/nav/nav';


@Component({
  templateUrl: 'app.html'
})
export class MyApp {
  @ViewChild(Nav) nav: Nav;
  rootPage = HomePage;
  pages: Array<{title: string, component: any}>;

 
  constructor(platform: Platform, public menu: MenuController) {
    platform.ready().then(() => {
      // Okay, so the platform is ready and our plugins are available.
      // Here you can do any higher level native things you might need.
      StatusBar.styleDefault();
      Splashscreen.hide();
    });

    this.pages = [
      { title: 'Home', component: HomePage },
      { title: 'Nav', component: NavPage }
    ];
  }

  openPage(page) {
    this.menu.close();

    this.nav.setRoot(page.component);
  }
}
