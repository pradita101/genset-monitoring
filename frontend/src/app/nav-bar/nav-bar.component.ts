import { Component, ViewChild, ElementRef, OnInit } from '@angular/core';

@Component({
  selector: 'nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.scss']
})
export class NavBarComponent implements OnInit {

  constructor() { }
  @ViewChild('navBurger',  {static: false}) navBurger: ElementRef;
  @ViewChild('navMenu',  {static: false}) navMenu: ElementRef;
  user_type = (localStorage.getItem('user_type') !== null) ?  localStorage.getItem('user_type') : "";
  login = false ;



  ngOnInit() {
    this.user_type = (localStorage.getItem('user_type') !== "") ?  localStorage.getItem('user_type') : "";
    this.login = (localStorage.getItem('login') !== null && localStorage.getItem('login') === 'true') ? true : false ;
  }

  toggleNavbar() {
    this.navBurger.nativeElement.classList.toggle('is-active');
    this.navMenu.nativeElement.classList.toggle('is-active');
  }

}
