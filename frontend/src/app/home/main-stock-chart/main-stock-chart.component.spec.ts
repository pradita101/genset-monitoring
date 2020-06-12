import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MainStockChartComponent } from './main-stock-chart.component';

describe('MainStockChartComponent', () => {
  let component: MainStockChartComponent;
  let fixture: ComponentFixture<MainStockChartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MainStockChartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MainStockChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
