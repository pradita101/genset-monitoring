import { Component, OnInit } from "@angular/core";
import { Chart } from "angular-highcharts";
import { webSocket } from "rxjs/webSocket";
import { GeneralFunctionService } from "../../general-function.service";
import { Web_Socket_Server } from "../../global";

@Component({
  selector: "main-chart",
  templateUrl: "./main-chart.component.html",
  styleUrls: ["./main-chart.component.scss"]
})
export class MainChartComponent implements OnInit {

  subject = webSocket(Web_Socket_Server);
  idS: Array<any> = [];
  mainChart = new Chart({
    title: {
      text: 'Gensets Temperature'
    },
    xAxis:{
      type: 'datetime',
      tickPixelInterval: 86400
    },
    yAxis:{
      title:{
        text: 'Temperature'
      }
    },
    credits: {
      enabled: false
    },
    series: []
  });

  constructor(
    private gf : GeneralFunctionService
  ) {}

  async add_point(tempData: any) {

    var additionalSeries;
    var checkData = this.idS.includes(tempData.A);
    var timestamp = await this.gf.countLocaltime(parseInt(tempData.B));

    if (checkData == false) {
      if(tempData.Id != undefined){
        additionalSeries = await {
          id: tempData.Id,
          tooltip: {
            valueDecimals: 2
          },
          type: 'spline',
          name: tempData.A,
          data: [
            [timestamp,parseFloat(tempData.G)]
          ]
        };
        this.mainChart.addSeries(additionalSeries,true,true);
        this.idS.push(tempData.A);
      }
    } else if(checkData == true){
      var position = await this.idS.indexOf(tempData.A);
        this.mainChart.addPoint([timestamp, parseFloat(tempData.G)],position);
    }


  }

  ngOnInit() {
    this.gf.checkSession();
    try {
      this.subject.subscribe(
        async mChartMsg => this.add_point(mChartMsg), // Called whenever there is a message from the server.
        err => console.log(err), // Called if at any point WebSocket API signals some kind of error.
        () => console.log('complete') // Called when connection is closed (for whatever reason).
      );
    } catch (error) {
      console.log(error);
    }
  }
}
