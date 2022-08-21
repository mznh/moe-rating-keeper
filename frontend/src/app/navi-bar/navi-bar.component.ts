import { Component, OnInit } from '@angular/core';
import {MatToolbarModule} from '@angular/material/toolbar';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-navi-bar',
  templateUrl: './navi-bar.component.html',
  styleUrls: ['./navi-bar.component.css']
})
export class NaviBarComponent implements OnInit {
  //key:string;

  constructor(private route: ActivatedRoute) {
    //this.route.queryParams.subscribe(
    //  (params:any) => {
    //    this.key = params.key;
    //  }
    //)
  }
  ngOnInit(): void {
    //this.route.queryParams.subscribe(
    //  (params:any) => {
    //    this.key = params.key;
    //  }
    //)
  }
}
