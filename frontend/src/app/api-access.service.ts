import { Injectable } from "@angular/core";
import { Observable, throwError, from } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { GensetData } from './genset-data';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Web_Server } from "./global";

@Injectable({
  providedIn: "root"
})

export class ApiAccessService {
  constructor(private http: HttpClient) {}
  endpoint: string = Web_Server;
  token = localStorage.getItem('token');
  headers = new HttpHeaders({'Content-Type': 'application/json', 'Authorization' : this.token});
  options = {headers: this.headers};
  username = localStorage.getItem('username');


  public toTimestamp(strDate) {
    var datum = Date.parse(strDate);
    return datum / 1000;
  }

  GetAllGenset(): Observable<any>{
    let local_token = localStorage.getItem('token');
    let local_headers = new HttpHeaders({'Content-Type': 'application/json', 'Authorization' : local_token});
    let local_options = {headers: local_headers};
    return this.http.get(`${this.endpoint}/genset_all/`, local_options);
  }

  GetDataGenset(id: string): Observable<any>{
    let API_URL = `${this.endpoint}/genset/`+id;
    return this.http.get(API_URL,this.options)
      .pipe(
        catchError(this.errorMgmt)
      )
  }

  GetStreamGenset(id:string): Observable<any>{
    let API_URL = `${this.endpoint}/stream_genset/`+id;
    return this.http.get(API_URL,this.options)
      .pipe(
        catchError(this.errorMgmt)
      )
  }

  AddGenset(data: GensetData): Observable<any> {
    let API_URL = `${this.endpoint}/genset/`;
    return this.http.post(API_URL, data,this.options)
      .pipe(
        catchError(this.errorMgmt)
      )
  }

  UpdateGenset(data: GensetData): Observable<any> {
    let API_URL = `${this.endpoint}/update_genset/`;
    return this.http.post(API_URL, data,this.options)
      .pipe(
        catchError(this.errorMgmt)
      )
  }

  DeleteGenset(id: any):Observable<any>{
    let API_URL = `${this.endpoint}/genset/`+id;
    return this.http.delete(API_URL, this.options)
      .pipe(
        catchError(this.errorMgmt)
      )
  }

  GetAllStream() {
    return this.http.get(`${this.endpoint}/stream_all/`);
  }

  GetStreamData(data: any){
    let API_URL = `${this.endpoint}/stream/`;
    return this.http.post(API_URL, data,this.options)
      .pipe(
        catchError(this.errorMgmt)
      )
  }

  GetAverage(data: any){
    let API_URL = `${this.endpoint}/avg_temp/`;
    return this.http.post(API_URL, data,this.options)
    .pipe(
      catchError(this.errorMgmt)
    )
  }

  AddUsers(data: any){
    let API_URL = `${this.endpoint}/add_user/`;
    return this.http.post(API_URL, data,this.options)
    .pipe(
      catchError(this.errorMgmt)
    )
  }

  errorMgmt(error: HttpErrorResponse) {
    let errorMessage = '';
    if (error.error instanceof ErrorEvent) {
      // Get client-side error
      errorMessage = error.error.message;
    } else {
      // Get server-side error
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    console.log(errorMessage);
    return throwError(errorMessage);
  }

}
