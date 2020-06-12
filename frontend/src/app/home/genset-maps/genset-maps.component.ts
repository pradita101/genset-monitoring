import { Component, OnInit } from '@angular/core';
import { webSocket } from "rxjs/webSocket";
import 'leaflet/dist/leaflet.css';
import * as L from 'leaflet';
import 'leaflet-defaulticon-compatibility';
import { Web_Socket_Server } from "../../global";
import { Router } from "@angular/router";
import { GeneralFunctionService } from "../../general-function.service";




@Component({
  selector: 'app-genset-maps',
  templateUrl: './genset-maps.component.html',
  styleUrls: ['./genset-maps.component.scss']
})

export class GensetMapsComponent implements OnInit {

  constructor(
    private gf : GeneralFunctionService,
    private router : Router
  ) { }
  mymap: any = null
  markers = {}
  subject = webSocket(Web_Socket_Server);
  icon = new L.Icon.Default();

  status: Boolean;


  async addMarker(data: any){

    var long, lat, genset_id,temperature
    lat = await data.C[0];
    long = await data.C[1];
    genset_id = await data.A;
    temperature = await parseFloat(data.Q).toFixed(2);


    if (!this.markers.hasOwnProperty(genset_id)) {
      this.markers[genset_id] = new L.Marker([lat, long]).addTo(this.mymap)
      .bindPopup('genset id: '+genset_id+'<br/> Temperature : '+temperature+' &deg;C')
      .openPopup();
      this.markers[genset_id].previousLatLngs = [];

    } else {
      this.markers[genset_id].previousLatLngs.push(this.markers[genset_id].getLatLng());
      this.markers[genset_id].setLatLng([lat, long])
      .bindPopup('genset id: '+genset_id+'<br/> Temperature : '+temperature+' &deg;C')
      .openPopup();
    }

  }


  ngOnInit() {

    this.gf.checkSession();
    this.status = (localStorage.getItem('login') === 'true') ? true : false;
    if(!this.status){
      this.router.navigate(['/login']);
    }

    this.icon.options.shadowSize = [0,0];
    this.mymap = L.map('gensetMap').setView([-2.833, 119.180], 5);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a> contributors'
    }).addTo(this.mymap);



    try {
      this.subject.subscribe(
        async mChartMsg => this.addMarker(mChartMsg), // Called whenever there is a message from the server.
        err => console.log(err), // Called if at any point WebSocket API signals some kind of error.
        () => console.log('complete') // Called when connection is closed (for whatever reason).
      );
    } catch (error) {
      console.log(error);
    }
  }

}
