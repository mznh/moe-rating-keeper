import { Component, OnInit } from '@angular/core';
import { MaterialsModule } from '../materials/materials.module';
import { RatingService } from '../rating-service/rating.service';
import { ActivatedRoute } from '@angular/router';
import { Observable, Subject,filter } from 'rxjs';
import { ResigterCharactorResult,CharactorInfo } from '../models/api-request';

@Component({
  selector: 'app-player-charactor-page',
  templateUrl: './player-charactor-page.component.html',
  styleUrls: ['./player-charactor-page.component.css']
})

export class PlayerCharactorPageComponent implements OnInit {
  
  


  constructor(private route: ActivatedRoute, private ratingService:RatingService) {
  }
  ngOnInit(): void {
    this.route.queryParams.subscribe(
      (params:any) => {
        console.log(params)
        this.ratingService.fetchPlayerCharactorInfo(params.key).subscribe(
          (data:CharactorInfo) =>{
            console.log(data);
          }
        );
      }
    )
  }
}

export interface Params{
  key:string;
};

