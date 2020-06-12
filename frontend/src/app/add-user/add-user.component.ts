import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { UsersType } from "../genset-data";
import { ApiAccessService } from "../api-access.service";
import { Router } from "@angular/router";

@Component({
  selector: 'add-user',
  templateUrl: './add-user.component.html',
  styleUrls: ['./add-user.component.scss']
})

export class AddUserComponent implements OnInit {

  constructor(
    private api : ApiAccessService,
    private fb: FormBuilder,
    private router : Router
  ) { }

  status: Boolean;
  userType: string;
  usersGroup: FormGroup;

  // usersGroup = new FormGroup({
  //   username: new FormControl(''),
  //   email: new FormControl(''),
  //   password: new FormControl(''),
  //   user_type: new FormControl(''),
  //   status: new FormControl('')
  // })

  usersType: Array<UsersType>;

  ngOnInit() {
    this.status = (localStorage.getItem('login') === 'true') ? true : false;
    this.userType = localStorage.getItem('user_type');

    if(!this.status){
      this.router.navigate(['/login']);
    }

    if(this.userType === 'user'){
      alert("You Lost ?");
      this.router.navigate(['/home']);
    }

    this.usersGroup = this.fb.group({
      username: ['', Validators.required],
      email: ['', Validators.required, Validators.email],
      password: ['', Validators.required],
      user_type: ['user', Validators.required],
      status: [1, Validators.required]
    });

    this.usersType = [
      new UsersType('admin','Admin'),
      new UsersType('user','Regular User'),
    ]
  }

  submitData(){
    this.api.AddUsers(this.usersGroup.value).subscribe(data => console.log(data), error => console.log(error));
  }

}
