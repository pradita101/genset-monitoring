import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TemperatureAlertComponent } from './temperature-alert.component';

describe('TemperatureAlertComponent', () => {
  let component: TemperatureAlertComponent;
  let fixture: ComponentFixture<TemperatureAlertComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TemperatureAlertComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TemperatureAlertComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
