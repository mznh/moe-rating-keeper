import { Component, OnInit, Input, ViewChild } from '@angular/core';
import { NaviBarComponent } from '../navi-bar/navi-bar.component';
import { MaterialsModule } from '../materials/materials.module';
import { RatingService } from '../rating-service/rating.service';
import { Observable, Subject } from 'rxjs';
import { RegisterCharactorResult } from '../models/api-request';
import { Router } from '@angular/router';
import { 
  SaveData, 
  PlayerData, 
  generateDefaultPlayerData} from '../models/data';

@Component({
  selector: 'app-register-page',
  templateUrl: './register-page.component.html',
  styleUrls: ['./register-page.component.css']
})
export class RegisterPageComponent implements OnInit {
  public charactorName:string;
  public charactorServer:string;
  public saveData:SaveData;

  constructor( private router:Router, private ratingService:RatingService) {
    this.saveData = this.ratingService.load();
    this.charactorName = "";
    this.charactorServer = "";
  }

  ngOnInit(): void {
  }

  submit(){
    this.ratingService.registerPlayerCharactor(this.charactorName,this.charactorServer).subscribe(
      (msg:RegisterCharactorResult) => {
        if(msg.status === "ok"){
          this.ratingService.saveNewPlayer(msg.player)
          console.log(this.saveData);
          this.router.navigate(["/pc"], {queryParams: {key: msg.player.key}});
        }
      }
    );
  }
  delete(){
    this.ratingService.deleteSaveData();
  }

  getPlayerKeyList(){
    return this.saveData.players.map((player:PlayerData) =>{
      return player.key
    })
  }

}
