import { TestBed } from '@angular/core/testing';

import { GeneralFunctionService } from './general-function.service';

describe('GeneralFunctionService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: GeneralFunctionService = TestBed.get(GeneralFunctionService);
    expect(service).toBeTruthy();
  });
});
