import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'logout-page',
  templateUrl: './logout-page.component.html',
  styleUrls: ['./logout-page.component.scss']
})
export class LogoutPageComponent implements OnInit {

  constructor() { }

  ngOnInit() {
    localStorage.clear()
  }

}
