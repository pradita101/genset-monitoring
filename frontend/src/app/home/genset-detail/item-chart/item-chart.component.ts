import { Component, OnInit, Input } from "@angular/core";
import { Chart } from "angular-highcharts";
import { webSocket } from "rxjs/webSocket";
import { Web_Socket_Server } from "../../../global";
import { ApiAccessService } from "../../../api-access.service";
import { GeneralFunctionService } from "../../../general-function.service"

@Component({
  selector: "item-chart",
  templateUrl: "./item-chart.component.html",
  styleUrls: ["./item-chart.component.scss"]
})
export class ItemChartComponent implements OnInit {
  @Input() engineId: string;

  subject = webSocket(Web_Socket_Server);
  chartInfo: string = "";
  locale = new Date().getTimezoneOffset();
  item_chart: Chart;

  async add_point(temp_data) {
    let timestamp, point,tempChart,rpmChart,powerChart,temp,speed,power,cek_speed;
    point = temp_data.Q;
    timestamp = await this.gf.countLocaltime(parseInt(temp_data.B));
    if(this.chartInfo){
      if (temp_data.A === this.engineId) {
        temp = [timestamp,parseFloat(point)];
        cek_speed = Math.round(parseFloat(temp_data.P)/1000);
        speed = [timestamp,parseFloat(cek_speed)];
        power = [timestamp,parseFloat(temp_data.L[0])];
        this.item_chart.addPoint(temp,0);
        this.item_chart.addPoint(speed,1);
        this.item_chart.addPoint(power,2);
      }
    }else{
      var now = Date.now();
      temp = [];
      speed = [];
      power = [];
      this.chartInfo = this.engineId;
      tempChart = {
        type: "spline",
        tooltip: {
          valueDecimals: 2
        },
        name: "Coolant Temp",
        data: [temp]
      }
      rpmChart = {
        type: "spline",
        tooltip: {
          valueDecimals: 2
        },
        name: "Engine Speed(in thousands)",
        data: [speed]
      }
      powerChart = {
        type: "spline",
        tooltip: {
          valueDecimals: 2
        },
        name: "Power Output",
        data: [power]
      }
      this.item_chart.addSeries(tempChart,true,true);
      this.item_chart.addSeries(rpmChart,true,true);
      this.item_chart.addSeries(powerChart,true,true);
    }
  }


  constructor(private api: ApiAccessService, private gf : GeneralFunctionService) {}

  ngOnInit() {
    this.gf.checkSession();
    if(this.engineId){
      this.initChart()
    }
    try {
      this.subject.subscribe(
        async msg => this.add_point(msg), // Called whenever there is a message from the server.
        err => console.log(err), // Called if at any point WebSocket API signals some kind of error.
        () => console.log("complete") // Called when connection is closed (for whatever reason).
      );
    } catch (error) {
      console.log(error);
    }
  }

  initChart(){
    this.item_chart = new Chart({
      title: {
        text: "Realtime Genset "+this.engineId+" Temperature"
      },
      credits: {
        enabled: false
      },
      xAxis:{
        tickPixelInterval: 7200,
        type: "datetime"
      },
      yAxis:{
        title:{
          text:'Temperature'
        }
      },
      series: []
    });
  }
}
