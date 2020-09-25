import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  url: string = 'http://localhost:9090/api/flights';
  constructor(private http: HttpClient) { }


}
