import { Component, OnInit } from '@angular/core';
import { webSocket } from "rxjs/webSocket";
import { Web_Socket_Server } from "../../global";
import * as moment from 'moment';
import { GeneralFunctionService } from "../../general-function.service"


@Component({
  selector: 'data-feed',
  templateUrl: './data-feed.component.html',
  styleUrls: ['./data-feed.component.scss']
})
export class DataFeedComponent implements OnInit {

  constructor(private gf : GeneralFunctionService) { }

  subject = webSocket(Web_Socket_Server);

  feeds = [];

  async add_feed(data){
    var maxData = 10
    if(this.feeds.length > maxData ){
      this.feeds = []
    }

    let A = await data.A;
    let tmp = await moment.unix(parseInt(data.B)).format("MM/DD/YYYY HH:mm:ss");
    let B = await moment(tmp).fromNow();
    let Q = await data.Q;
    let dataJson = await {'A':A,'B':B,'Q':Q};
    this.feeds.unshift(dataJson);


  }

  ngOnInit() {
    try {
      this.subject.subscribe(
        async msg => this.add_feed(msg), // Called whenever there is a message from the server.
        err => console.log(err), // Called if at any point WebSocket API signals some kind of error.
        () => console.log("complete") // Called when connection is closed (for whatever reason).
      );
    } catch (error) {
      console.log(error);
    }
  }

}
