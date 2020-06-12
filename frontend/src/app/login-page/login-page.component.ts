import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { loginData } from "../genset-data";
import { LoginService } from "../login.service";
import { Router } from "@angular/router";
import { GeneralFunctionService } from "../general-function.service";
import { Subscription } from 'rxjs';

@Component({
  selector: 'login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent implements OnInit, OnDestroy {

  constructor( private login : LoginService,
               private router : Router,
               private fb: FormBuilder,
               private gf : GeneralFunctionService
              ) { }

  loginGroup : FormGroup

  dataLogin : loginData;
  status : Boolean;

  subscription : Subscription;

  ngOnDestroy(){
    if(this.subscription){
      this.subscription.unsubscribe();
    }

  }


  ngOnInit() {
    this.gf.checkSession();
    this.status = (localStorage.getItem('login') === 'true') ? true : false;

    if(this.status){
      this.router.navigate(['/home']);
    }

    this.loginGroup = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });

  }

  loginAction(){
    this.subscription = this.login.getLoginData(this.loginGroup.value).subscribe(
      result => this.loginRoutine(result),
      err => console.log(err),
      () => this.router.navigate(['/home'])
    );
  }


  async loginRoutine(data){
    var now = await new Date().getTime();
    var expiry = await now + ((2*60)*(60*1000))
    var user_data = await JSON.parse(data.data);
    localStorage.setItem('login',data.status);
    localStorage.setItem('token', data.token);
    localStorage.setItem('user_type', user_data[0].users_user_type);
    localStorage.setItem('username', user_data[0].users_username);
    localStorage.setItem('org', user_data[0].users_organization);
    localStorage.setItem('expiry', expiry.toString());
  }

}
