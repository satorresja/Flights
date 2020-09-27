import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Response } from '../models/response';
import { map } from 'rxjs/operators';



@Injectable({
  providedIn: 'root'
})
export class ResultsService {

  url: string = 'http://127.0.0.1:8080/api/flights/';

  constructor(private http: HttpClient) { }

  public getResults(input: string): Observable<Response[]> {

    return this.http.get(this.url.concat(input)).pipe(map(response => response as Response[]));
  }
}
