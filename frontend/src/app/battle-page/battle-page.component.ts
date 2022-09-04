import { Component, OnInit, OnChanges } from '@angular/core';
import { MaterialsModule } from '../materials/materials.module';
import { RatingService } from '../rating-service/rating.service';
import { ActivatedRoute } from '@angular/router';
import { Observable, Subject,filter } from 'rxjs';
import { RegisterCharactorResult} from '../models/api-request';
import { SaveData, PlayerData, generateDefaultPlayerData} from '../models/data';

@Component({
  selector: 'app-battle-page',
  templateUrl: './battle-page.component.html',
  styleUrls: ['./battle-page.component.css']
})
export class BattlePageComponent implements OnInit {
  saveData:SaveData;
  // for display
  player:PlayerData = generateDefaultPlayerData();
  // for input
  opponentName:string = "";
  opponentToken:string = "";

  constructor(private route: ActivatedRoute, private ratingService:RatingService) {
    this.saveData = this.ratingService.load();
  }

  ngOnInit(): void {
    this.route.queryParams.subscribe(
      (params:any) => {
        console.log(params)
        // query strings に key があれば情報を取得
        if( "key" in params){
          this.ratingService.fetchPlayerCharactorInfo(params.key).subscribe(
            (data:PlayerData) =>{
              this.player = data;
              console.log("pc page info");
              console.log(data);
            }
          );
        }
      }
    )
  }

  ngOnChanges():void{
  }

  submit(){
    console.log( this.player)
    console.log( this.opponentName, this.opponentToken)
    this.ratingService.recordBattleResult({
      side_a_name: this.player.name,
      side_a_token:this.player.token,
      side_b_name: this.opponentName,
      side_b_token:this.opponentToken,
      winner_token:this.player.token
    }).subscribe(
      (res:any) =>{
        console.log(res)
      }
    );
  }

}
