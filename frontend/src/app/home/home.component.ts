import { Component, OnInit } from "@angular/core";
import { ApiAccessService } from "../api-access.service";
import { GeneralFunctionService } from "../general-function.service";
import { Router } from "@angular/router";



@Component({
  selector: "app-home",
  templateUrl: "./home.component.html",
  styleUrls: ["./home.component.scss"]
})

export class HomeComponent implements OnInit {
  constructor(private api: ApiAccessService, private gf : GeneralFunctionService, private router : Router) {}
  EngineCode: string;
  status = false;
  ids = []
  rows = []

  async addGensetId(data){
    let item, gensetData;
    gensetData = await data;
    if(gensetData){
      for(let i = 0; i < gensetData.length; i++){
        item = gensetData[i]
        this.ids.push(item.genset_ASI_genset_id);
     }
     this.rows = this.gf.chunkArray(this.ids, 3)
    }
  }

  ngOnInit() {
    this.gf.checkSession();
    this.status = (localStorage.getItem('login') === 'true') ? true : false;
    if(this.status !== true){
      this.router.navigate(['/login']);
    }else{
      this.api.GetAllGenset().subscribe(result => this.addGensetId(JSON.parse(result.data)))
    }
  }

}
