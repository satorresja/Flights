import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ResultsService } from './results.service';
import { Response } from '../models/response';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {

  params: string;
  responses: Response[];

  constructor(private activatedRoute: ActivatedRoute, private resultsService: ResultsService) { }

  ngOnInit(): void {
    this.activatedRoute.paramMap.subscribe(result => {
      this.params = result.get('departure')+'/'+result.get('arrival')+'/'+result.get('date');
      this.resultsService.getResults(this.params).subscribe(flights => this.responses = flights)
    });
  }



}
