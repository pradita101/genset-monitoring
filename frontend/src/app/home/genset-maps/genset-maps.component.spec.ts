import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GensetMapsComponent } from './genset-maps.component';

describe('GensetMapsComponent', () => {
  let component: GensetMapsComponent;
  let fixture: ComponentFixture<GensetMapsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GensetMapsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GensetMapsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
