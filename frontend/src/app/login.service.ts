import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { catchError, map } from 'rxjs/operators';
import { Web_Server } from "./global";
import { Observable, throwError, from } from 'rxjs';
import { loginData } from "./genset-data";
import { ApiAccessService } from "./api-access.service";
import { Router } from "@angular/router";



@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient, private API: ApiAccessService) {}
  private endpoint: string = Web_Server;
  private headers = new HttpHeaders().set('Content-Type', 'application/json');
  private router : Router;

  getLoginData(data: loginData): Observable<any> {
    let API_URL = `${this.endpoint}/login/`;
    data.access = "Web"
    return this.http.post(API_URL, data)
      .pipe(
        catchError(this.API.errorMgmt)
      );
  }
  Logout(){
   localStorage.clear();
   this.router.navigate(['login'])
  }

}
