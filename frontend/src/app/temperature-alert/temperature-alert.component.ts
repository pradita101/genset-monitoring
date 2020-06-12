import { Component, OnInit } from '@angular/core';
import { webSocket } from "rxjs/webSocket";
import { Web_Socket_Server } from "../global";
import * as bulmaToast from "bulma-toast";


@Component({
  selector: 'temperature-alert',
  templateUrl: './temperature-alert.component.html',
  styleUrls: ['./temperature-alert.component.scss']
})
export class TemperatureAlertComponent implements OnInit {

  constructor() { }
  subject = webSocket(Web_Socket_Server);
  show = false;
  login = false

  async checkData(data:any){
    var alertHeat = 80;
    if(parseFloat(data.Q) >= alertHeat){
      var temp = parseFloat(data.Q).toFixed(2);
      bulmaToast.toast({
        message: "Attention Genset With Code <strong>"+data.A+"</strong> Is Over Heat With Temperature : <strong>"+temp+" &deg; C</strong>",
        type: "is-danger",
        duration: 5000,
        dismissible: true,
        closeOnClick: true,
        pauseOnHover: true,
        animate: { in: "fadeIn", out: "fadeOut" }
      });
    }
  }

  buttonClicked(){
    this.show = false;
  }

  ngOnInit() {
    this.login = (localStorage.getItem('login') !== null && localStorage.getItem('login') === 'true') ? true : false ;
    if(this.login === true){

      try {
        this.subject.subscribe(
          async mChartMsg => this.checkData(mChartMsg), // Called whenever there is a message from the server.
          err => console.log(err), // Called if at any point WebSocket API signals some kind of error.
          () => console.log('complete') // Called when connection is closed (for whatever reason).
        );
      } catch (error) {
        console.log(error);
      }
    }
  }

}
