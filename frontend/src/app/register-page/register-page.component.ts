import { Component, OnInit, Input, ViewChild } from '@angular/core';
import { NaviBarComponent } from '../navi-bar/navi-bar.component';
import { MaterialsModule } from '../materials/materials.module';
import { RatingService } from '../rating-service/rating.service';
import { Observable, Subject } from 'rxjs';
import { ResigterCharactorResult } from '../models/api-request';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register-page',
  templateUrl: './register-page.component.html',
  styleUrls: ['./register-page.component.css']
})
export class RegisterPageComponent implements OnInit {
  public charactorName:string;
  public charactorServer:string;

  constructor( private router:Router, private ratingService:RatingService) {
    this.charactorName = "";
    this.charactorServer = "";
  }

  ngOnInit(): void {
  }

  submit(){
    this.ratingService.registerPlayerCharactor(this.charactorName,this.charactorServer).subscribe(
      (msg:ResigterCharactorResult) => {
        if(msg.status === "ok"){
          this.router.navigate(["/pc"], {queryParams: {key: msg.key}});
        }
      }
    );
  }

}
