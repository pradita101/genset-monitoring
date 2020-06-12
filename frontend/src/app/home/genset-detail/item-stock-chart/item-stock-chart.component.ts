import { Component, OnInit, Input } from '@angular/core';
import { StockChart } from "angular-highcharts";
import { GeneralFunctionService } from '../../../general-function.service';
import { ApiAccessService } from "../../../api-access.service";
import { NgxSpinnerService } from "ngx-spinner";

@Component({
  selector: 'item-stock-chart',
  templateUrl: './item-stock-chart.component.html',
  styleUrls: ['./item-stock-chart.component.scss']
})
export class ItemStockChartComponent implements OnInit {

  constructor(
    private gf : GeneralFunctionService,
    private api: ApiAccessService,
    private loader: NgxSpinnerService
  ) { }

  @Input() engineId: string;
  stockChart : StockChart;
  result: any;
  load = 1;


  ngOnInit() {
    this.gf.checkSession();
    this.loader.show();
    this.api.GetStreamGenset(this.engineId).subscribe(result => this.generateStreamData(JSON.parse(result.data)))
  }

  async initCharts(){
    this.stockChart = new StockChart({
      rangeSelector: {
        selected: 1
      },
      title: {
        text: 'Historical Temperature Chart Genset '+this.engineId
      },
      series: [
          {
        tooltip: {
          valueDecimals: 2
        },
        type: 'spline',
        name: this.engineId,
        data: this.result
      }]
    });
    this.load = 0;
    this.loader.hide();
  }

  async generateStreamData(datas){
    this.result = await this.gf.exctractStream(datas);
    if(this.result){
      this.initCharts()
    }

  }

}
