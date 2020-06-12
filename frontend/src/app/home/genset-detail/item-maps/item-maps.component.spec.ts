import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ItemMapsComponent } from './item-maps.component';

describe('ItemMapsComponent', () => {
  let component: ItemMapsComponent;
  let fixture: ComponentFixture<ItemMapsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ItemMapsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ItemMapsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
