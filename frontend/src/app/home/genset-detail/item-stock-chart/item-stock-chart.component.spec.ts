import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ItemStockChartComponent } from './item-stock-chart.component';

describe('ItemStockChartComponent', () => {
  let component: ItemStockChartComponent;
  let fixture: ComponentFixture<ItemStockChartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ItemStockChartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ItemStockChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
