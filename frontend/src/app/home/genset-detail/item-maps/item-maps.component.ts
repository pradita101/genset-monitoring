import { Component, OnInit, Input } from '@angular/core';
import { ApiAccessService } from "../../../api-access.service";
import * as moment from 'moment';
import 'leaflet/dist/leaflet';
declare var L : any;
import 'leaflet-defaulticon-compatibility';
import 'leaflet.polyline.snakeanim/L.Polyline.SnakeAnim';

@Component({
  selector: 'item-maps',
  templateUrl: './item-maps.component.html',
  styleUrls: ['./item-maps.component.scss']
})
export class ItemMapsComponent implements OnInit {
  @Input() engineId: string;


  constructor(private api : ApiAccessService) { }
  path = []
  data: any = null;
  itemsMap: any = null
  gensetData: object;
  endDate = moment().format('YYYY-MM-DD') + " 23:59:59"
  startDate = moment().subtract(7,'d').format('YYYY-MM-DD') + " 00:01:00"
  filterDate: any;
  layers: any;
  markers: any;


  ngOnInit() {

    L.Map.include({
      'clearLayers': function () {
        this.eachLayer(function (layer) {
          this.removeLayer(layer);
        }, this);
      }
    });

    this.itemsMap = L.map('items-map').setView([-3.557, 112.192], 5);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a> contributors'
    }).addTo(this.itemsMap);
    let send_data = {
      id: this.engineId,
      start_date: this.startDate,
      end_date: this.endDate
    }

    this.api.GetStreamData(send_data).subscribe(result => this.constructMaps(result))
  }

  onClick(){

    if (typeof this.layers !== "undefined") {
      this.itemsMap.removeLayer(this.layers)
    }

    var mstart = moment(this.filterDate[0])
    var mend = moment(this.filterDate[1])
    var comparedate = mstart.isBefore(mend)
    if(! comparedate){
      alert("start date is after end date, please check")
      return false
    }
    this.startDate = moment(this.filterDate[0]).format('YYYY-MM-DD HH:mm:SS');
    this.endDate = moment(this.filterDate[1]).format('YYYY-MM-DD HH:mm:SS');

    let post_data = {
      id : this.engineId,
      start_date: this.startDate,
      end_date: this.endDate
    }
    this.path = []
    this.api.GetStreamData(post_data).subscribe(res => this.constructMaps(res))
  }

  async constructMaps(data){
    if(data.data){
      var parseData = JSON.parse(data.data);
      parseData.forEach(item => {
        let temp = [item.data_stream_ASI_latitude,item.data_stream_ASI_longitude]
        this.path.push(temp)
      });

      if(this.path){

        this.layers = L.layerGroup([
          L.marker(this.path[0]),
          L.polyline(this.path),
          L.marker(this.path[this.path.length - 1])
          ], { snakingPause: 200 });
          this.layers.addTo(this.itemsMap).snakeIn();
      }
    }
  }

}
