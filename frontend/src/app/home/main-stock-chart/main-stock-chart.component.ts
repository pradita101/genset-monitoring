import { Component, OnInit, Input } from '@angular/core';
import { StockChart } from "angular-highcharts";
import { GeneralFunctionService } from '../../general-function.service';
import { ApiAccessService } from "../../api-access.service";

@Component({
  selector: 'main-stock-chart',
  templateUrl: './main-stock-chart.component.html',
  styleUrls: ['./main-stock-chart.component.scss']
})
export class MainStockChartComponent implements OnInit {

  constructor(
    private gf : GeneralFunctionService,
    private api: ApiAccessService
  ) { }

  @Input() engineIds: Array<string>;
  stockChart : StockChart;
  data_series : any;
  series  = [];

  ngOnInit() {
    this.gf.checkSession();
    if(this.engineIds){
      this.create_series(this.engineIds);
    }
  }

  async initCharts(){
    this.stockChart = new StockChart({
      rangeSelector: {
        selected: 1
      },
      title: {
        text: 'Historical Temperature Chart'
      },
      series: this.series
    });
  }

  async create_series(engineId : Array<string>){
    this.api.GetAllStream().subscribe(result => this.generateStreamData(result, engineId))
  }

  async generateStreamData(datas, engineId){
    this.data_series = await this.gf.exctractAllStream(JSON.parse(datas.data), engineId);
    var idx = 0;
    var seriesIndex;
    for (idx = 0; idx < engineId.length; idx ++) {
      seriesIndex = engineId.indexOf(engineId[idx]);
      let itemSeries = {
        tooltip: {
          valueDecimals: 2
        },
        type: 'spline',
        name: engineId[idx],
        data: this.data_series[seriesIndex]
      }
      this.series.push(itemSeries)
    }

    if(this.series){
      this.initCharts()
    }

  }

}
