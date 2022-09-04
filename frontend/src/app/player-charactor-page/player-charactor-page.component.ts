import { Component, OnInit, OnChanges } from '@angular/core';
import { MaterialsModule } from '../materials/materials.module';
import { RatingService } from '../rating-service/rating.service';
import { ActivatedRoute } from '@angular/router';
import { Observable, Subject,filter } from 'rxjs';
import { 
  RegisterCharactorResult,
  ResultOfFetchBattle,
} from '../models/api-request';
import { 
  SaveData, 
  BattleData,
  PlayerData, generateDefaultPlayerData} from '../models/data';

@Component({
  selector: 'app-player-charactor-page',
  templateUrl: './player-charactor-page.component.html',
  styleUrls: ['./player-charactor-page.component.css']
})

export class PlayerCharactorPageComponent implements OnInit {
  nowSelectPlayerId:string = "";
  player:PlayerData = generateDefaultPlayerData();
  saveData:SaveData;
  battleDataList:BattleData[] = [];

  constructor(private route: ActivatedRoute, private ratingService:RatingService) {
    this.saveData = this.ratingService.load();
  }
  ngOnInit(): void {
    this.route.queryParams.subscribe(
      (params:any) => {
        console.log(params)
        if( "key" in params){
          this.ratingService.fetchPlayerCharactorInfo(params.key).subscribe(
            (data:PlayerData) =>{
              this.player = data;
              this.updateBattleLogs()
              this.ngOnChanges()
              console.log("pc page info");
              console.log(data);
            }
          );
        }
      }
    )
  }
  ngOnChanges(): void {
    this.updateBattleLogs()
  }
  updateBattleLogs(){
    this.ratingService.fetchBattleResultByPlayer(this.player.key).subscribe(
      (res:ResultOfFetchBattle)=>{
        this.battleDataList = res.battles
        console.log("resrerersr")
        console.log(res)
    })
  }
}



export interface Params{
  key:string;
};

