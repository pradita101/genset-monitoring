import { Component, OnInit, Input } from "@angular/core";
import { webSocket } from "rxjs/webSocket";
import { WsData } from "../../ws-data";
import { Web_Socket_Server } from "../../global";
import { Router } from '@angular/router';

@Component({
  selector: "info-card",
  templateUrl: "./info-card.component.html",
  styleUrls: ["./info-card.component.scss"]
})
export class InfoCardComponent implements OnInit {
  @Input() engineId: any;

  info: string;
  temperature: number = 0;
  engineStatus: any = 0;
  oilPressure: any = 0;
  engineSpeed: any = 0;
  powerOutput: any = 0;
  outputStream: any = 0;
  vol1Phase: any = 0;
  vol3Phase: any = 0;
  frequency: any = 0;
  bateryVoltage: any = 0;
  gensetMode: any;
  EngineCode: string;
  fuelConsuption: number = 0;
  EngHour: number = 0;
  subject = webSocket(Web_Socket_Server);
  ws_message: Object;
  genset: Array<any> = [];
  // router: string;

  constructor(
    private router: Router
  ) {}

  async onReceiveData(data) {
    let data_in: WsData = await data;
    if (this.engineId === data_in.A) {
      this.temperature = parseFloat(data_in.Q);
      this.engineStatus = data_in.I;
      this.EngineCode = data_in.A;
      this.fuelConsuption = parseFloat(data_in.N);
      this.EngHour = parseInt(data_in.F);
      this.engineSpeed = parseFloat(data_in.P);
      this.oilPressure = parseFloat(data_in.O);
      this.powerOutput = parseFloat(data_in.L[0]);
      this.outputStream = parseFloat(data_in.T);
      this.vol1Phase = parseFloat(data_in.K[0]);
      this.vol3Phase = parseFloat(data_in.K[2]);
      this.frequency = parseFloat(data_in.U);
      this.bateryVoltage = parseFloat(data_in.H);
      this.gensetMode = data_in.V;

      if (this.genset) {
        let search = this.genset.indexOf(this.EngineCode);
        if (search < 0) {
          this.genset.push(this.EngineCode);
        }
      } else {
        this.genset.push(this.EngineCode);
      }
    }
  }

  ngOnInit() {
    // this.router = "/details/"+this.engineId;
    try {
      this.subject.subscribe(
        async msg => this.onReceiveData(msg), // Called whenever there is a message from the server.
        err => console.log(err), // Called if at any point WebSocket API signals some kind of error.
        () => console.log("complete") // Called when connection is closed (for whatever reason).
      );
    } catch (error) {
      console.log(error);
    }
  }
  gotoDetails(id:string){
    this.router.navigate(['/details', this.engineId])
  }
}
