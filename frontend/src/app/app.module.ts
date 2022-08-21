import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';

import { RegisterPageComponent } from './register-page/register-page.component';
import { PlayerCharactorPageComponent } from './player-charactor-page/player-charactor-page.component';
import { BattlePageComponent } from './battle-page/battle-page.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NaviBarComponent } from './navi-bar/navi-bar.component';

import { MaterialsModule } from './materials/materials.module';


@NgModule({
  declarations: [
    AppComponent,
    RegisterPageComponent,
    PlayerCharactorPageComponent,
    BattlePageComponent,
    NaviBarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MaterialsModule,
    BrowserAnimationsModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
