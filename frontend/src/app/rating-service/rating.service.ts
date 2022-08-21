import { Injectable } from '@angular/core';
import { Observable, of, Subject } from "rxjs";
import { webSocket } from "rxjs/webSocket";
import { mergeMap, map, catchError } from "rxjs/operators";
import { HttpClient,HttpHeaders, HttpParams,HttpParamsOptions } from '@angular/common/http';
import { ResigterCharactorResult,CharactorInfo } from '../models/api-request';

@Injectable({
  providedIn: 'root'
})
export class RatingService {
  API_URL:string = "http://localhost:8000/v1"; 

  constructor(private http:HttpClient) {
  }

  public generateHttpHeader(){
    return {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
      })
    };
  }

  public registerPlayerCharactor(name:string, server:string):Observable<ResigterCharactorResult>{
    const targetUrl = this.API_URL + "/player"
    const body = {
      name: name,
      server: server
    }
    return  this.http.post<ResigterCharactorResult>(targetUrl,body,this.generateHttpHeader());
  }

  public fetchPlayerCharactorInfo(key:string):Observable<CharactorInfo >{
    const targetUrl = this.API_URL + "/player"
    const options = {
      headers: new HttpHeaders({ 'Access-Control-Allow-Origin': '*', }),
      params: new HttpParams(<HttpParamsOptions>{fromObject:{ "key": key }}),
    }
    return  this.http.get<CharactorInfo>(targetUrl, options)
  }
}
