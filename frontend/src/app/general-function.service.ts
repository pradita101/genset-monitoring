import { Injectable } from '@angular/core';
import { Router } from "@angular/router";

@Injectable({
  providedIn: 'root'
})
export class GeneralFunctionService {

  constructor(private router: Router) { }

  chunkArray(myArray, chunk_size){
    var index = 0;
    var arrayLength = myArray.length;
    var tempArray = [];
    var myChunk;

    for (index = 0; index < arrayLength; index += chunk_size) {
        myChunk = myArray.slice(index, index+chunk_size);
        // Do something if you want with the group
        tempArray.push(myChunk);
    }
    return tempArray;
  }

  async exctractStream(datas){
    var arrayLength = datas.length;
    var temp,data, timestamp;
    var result = [];
    var i = 0

    for (i = 0; i < arrayLength; i ++) {
      temp = datas[i];
      timestamp = await this.countLocaltime(parseInt(temp.data_stream_ASI_timestamp));
      data = [parseInt(timestamp), parseFloat(temp.data_stream_ASI_temperature)];
      result.push(data);
    }
    return result;
  }

  async exctractAllStream(datas, engineIds: Array<string>){
    var arrayLength = datas.length;
    var temp,data, timestamp;
    var result  = [];
    var i = 0 ;
    var a = 0;
    var seriesIndex;

    for (a = 0; a < engineIds.length; a ++) {
      result.push([])
    }

    for (i = 0; i < arrayLength; i ++) {
      temp = datas[i];
      seriesIndex = engineIds.indexOf(temp.data_stream_ASI_genset_id);
      timestamp = await this.countLocaltime(parseInt(temp.data_stream_ASI_timestamp));
      data = [parseInt(timestamp), parseFloat(temp.data_stream_ASI_temperature)];
      result[seriesIndex].push(data);
    }
    return result;
  }

  async countLocaltime(valTime:number){
    var locale = new Date().getTimezoneOffset();
    var local = locale * -1 ;
    var timestamp = valTime * 1000 + ( ( local * 60 ) * 1000);
    return timestamp;
  }

  async checkSession(){
    var expiry = await localStorage.getItem('expiry');
    var now = await new Date().getTime();
    if(now >= parseInt(expiry)){
      localStorage.clear();
      this.router.navigate([''])
    }
  }
}
