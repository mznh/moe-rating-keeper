import { Injectable } from '@angular/core';
import { Observable, of, Subject } from "rxjs";
import { webSocket } from "rxjs/webSocket";
import { mergeMap, map, catchError } from "rxjs/operators";
import { HttpClient,HttpHeaders, HttpParams,HttpParamsOptions } from '@angular/common/http';
import { SaveData,PlayerData,generateDefaultSaveData } from '../models/data';
import {
  RegisterCharactorResult,
  ResultOfRecordBattle,
  RequestOfRecordBattle,
  ResultOfFetchBattle
} from '../models/api-request';

const localStorageKey = "MoERatingCharactors"


@Injectable({
  providedIn: 'root'
})
export class RatingService {
  API_URL:string = "http://localhost:8000"; 
  saveData:SaveData = generateDefaultSaveData();

  constructor(private http:HttpClient) {
  }

  public generateHttpHeader(){
    return {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
      })
    };
  }

  public registerPlayerCharactor(name:string, server:string):Observable<RegisterCharactorResult>{
    const targetUrl = this.API_URL + "/player"
    const body = {
      name: name,
      server: server
    }
    return  this.http.post<RegisterCharactorResult>(targetUrl,body,this.generateHttpHeader());
  }

  public fetchPlayerCharactorInfo(key:string):Observable<PlayerData>{
    const targetUrl = this.API_URL + "/player"
    //const options = {
    //  headers: new HttpHeaders({ 'Access-Control-Allow-Origin': '*', }),
    //  params: new HttpParams(<HttpParamsOptions>{fromObject:{ "key": key }}),
    //}
    const options ={
      params: new HttpParams(<HttpParamsOptions>{fromObject:{ "key": key }}),
      ...this.generateHttpHeader()
    }
    return  this.http.get<PlayerData>(targetUrl, options)
  }
  
  public recordBattleResult(reqBody:RequestOfRecordBattle){
    const targetUrl = this.API_URL + "/battle"
    return  this.http.post<ResultOfRecordBattle>(targetUrl,reqBody,this.generateHttpHeader());
  }

  public fetchBattleResultByPlayer(key:string):Observable<ResultOfFetchBattle>{
    const targetUrl = this.API_URL + "/battle"
    const options ={
      params: new HttpParams(<HttpParamsOptions>{fromObject:{ "key": key }}),
      ...this.generateHttpHeader()
    }
    return  this.http.get<ResultOfFetchBattle>(targetUrl, options);

  }

  public saveNewPlayer(player:PlayerData){
    this.saveData = this.load()
    this.saveData.players.push(player)
    const jsonString = JSON.stringify(this.saveData)
    localStorage.setItem(localStorageKey,jsonString)
    console.log("add new player");
    console.log(this.saveData);
    return this.saveData;
  }
  public load(){
    const saveRowStringData = localStorage.getItem(localStorageKey)
    if(saveRowStringData !== null){
      this.saveData = JSON.parse(saveRowStringData)
      console.log("load save data");
      console.log(this.saveData);
      return this.saveData
    }else {
      return generateDefaultSaveData();
    }
  }
  public deleteSaveData(){
    localStorage.removeItem(localStorageKey)
  }
}
