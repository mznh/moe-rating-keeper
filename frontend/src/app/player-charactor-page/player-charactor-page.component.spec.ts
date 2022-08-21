import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlayerCharactorPageComponent } from './player-charactor-page.component';

describe('PlayerCharactorPageComponent', () => {
  let component: PlayerCharactorPageComponent;
  let fixture: ComponentFixture<PlayerCharactorPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PlayerCharactorPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PlayerCharactorPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
