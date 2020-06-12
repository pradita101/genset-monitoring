import { Component, ViewChild, ElementRef, OnInit } from '@angular/core';

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"]
})
export class AppComponent {



  title = "Genset Monitoring";
  copyright_year = new Date().getFullYear();


}
