import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DataFeedComponent } from './data-feed.component';

describe('DataFeedComponent', () => {
  let component: DataFeedComponent;
  let fixture: ComponentFixture<DataFeedComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DataFeedComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DataFeedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
