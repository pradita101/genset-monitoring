import { Component, OnInit } from "@angular/core";
import { ActivatedRoute } from "@angular/router";
import { ApiAccessService } from "../../api-access.service";
import { FormBuilder, Validators } from '@angular/forms';
import { GensetSavedData, AvgTempData } from '../../genset-data';
import { Router } from "@angular/router";
import { GeneralFunctionService } from "../../general-function.service";

@Component({
  selector: "app-genset-detail",
  templateUrl: "./genset-detail.component.html",
  styleUrls: ["./genset-detail.component.scss"]
})
export class GensetDetailComponent implements OnInit {

  constructor(
    private _Activatedroute: ActivatedRoute,
    private API: ApiAccessService,
    private fb: FormBuilder,
    private gf: GeneralFunctionService,
    private router : Router
  ) {
    // this.reactiveForm();
  }

  id: any;
  name: any;
  data: GensetSavedData;
  gensetForm: any;
  showModals = 0;
  week = 0;
  month = 0;
  year = 0;
  map = 0;
  AvgData: AvgTempData;
  realtime = 1;
  historical = 0;
  status : Boolean;


  submitForm() {
    this.API.UpdateGenset(this.gensetForm.value).subscribe(data => console.log(data), error => console.log(error))
    this.closeModals()
  }

  async ngOnInit(){
    this.gf.checkSession();
    this.status = (localStorage.getItem('login') === 'true') ? true : false;
    if(!this.status){
      this.router.navigate(['/login']);
    }
    this.id = await this._Activatedroute.snapshot.params.id;
    if (this.id !== undefined) {
      this.API.GetDataGenset(this.id).subscribe(result => this.dataReceived(JSON.parse(result.data)))
      this.name = this.id
      this.gensetForm = this.fb.group({
        Id: [this.id, Validators.required],
        name: ['', Validators.required],
        detail: ['', Validators.required],
        tank_capacity: ['', Validators.required],
        displacement: ['', Validators.required],
        starting_system: ['', Validators.required],
        design_features: ['', Validators.required],
        full_load_consumption: ['', Validators.required],
        three_quarter_load_consumption: ['', Validators.required],
        half_load_consumption: ['', Validators.required],
        quarter_load_consumption: ['', Validators.required],
        bore_stroke: ['', Validators.required],
        continuous_rated_output: ['', Validators.required],
        voltage_allowance: ['', Validators.required]
      });
      this.weekClicked()
    }
    // if(this.data){
    //   alert("ada");
    // }else{
    //   alert("kosong");
    // }
  }


  closeModals() {
    this.showModals = 0;
  }

  openModals() {
    this.showModals = 1;
  }


  weekClicked() {
    this.week = 1;
    this.month = 0;
    this.year = 0;if(this.id!==undefined){
      let sendData = { 'period': 'week', 'genset_id': this.id }
    this.API.GetAverage(sendData).subscribe(avgResult => this.avgDataProcess(avgResult))
    }
  }

  monthClicked() {
    this.week = 0;
    this.month = 1;
    this.year = 0;
    if(this.id!==undefined){
      let sendData = { 'period': 'month', 'genset_id': this.id }
    this.API.GetAverage(sendData).subscribe(avgResult => this.avgDataProcess(avgResult))
    }
  }

  yearClicked() {
    this.week = 0;
    this.month = 0;
    this.year = 1;
    if(this.id!==undefined){
      let sendData = { 'period': 'year', 'genset_id': this.id }
    this.API.GetAverage(sendData).subscribe(avgResult => this.avgDataProcess(avgResult))
    }

  }

  realtimeClicked() {
    this.realtime = 1;
    this.historical = 0;
    this.map = 0;
  }

  historicalClicked() {
    this.realtime = 0;
    this.historical = 1;
    this.map = 0;
  }

  mapClicked() {
    this.realtime = 0;
    this.historical = 0;
    this.map = 1;
  }

  async avgDataProcess(data: any) {
    let temp = await JSON.parse(data.data)
    this.AvgData = await temp[0]
  }

  async dataReceived(data: Array<any>) {
    this.data = await data[0]
  }

}
