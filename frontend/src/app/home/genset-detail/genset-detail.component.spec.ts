import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GensetDetailComponent } from './genset-detail.component';

describe('GensetDetailComponent', () => {
  let component: GensetDetailComponent;
  let fixture: ComponentFixture<GensetDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GensetDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GensetDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
