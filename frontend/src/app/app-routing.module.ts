import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegisterPageComponent } from './register-page/register-page.component';
import { PlayerCharactorPageComponent } from './player-charactor-page/player-charactor-page.component';
import { BattlePageComponent } from './battle-page/battle-page.component';

const routes: Routes = [
  {path: "", component: RegisterPageComponent },
  {path: "register", component: RegisterPageComponent },
  {path: "pc", component: PlayerCharactorPageComponent },
  {path: "battle", component: BattlePageComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
