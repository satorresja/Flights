import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ResultsService } from './results.service';
import { Response } from '../models/response';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css'],
})
export class ResultsComponent implements OnInit {
  params: string;
  responses: Response[];
  numResponses: Number;
  best_ids: string[];
  worst_ids: string[];

  constructor(
    private activatedRoute: ActivatedRoute,
    private resultsService: ResultsService
  ) {}

  computeBest(results: Response[]): string[] {
    let prices: number[] = results.map((result) => result.price);
    let lowest = Math.min(...prices);
    return results
      .filter((result) => result.price === lowest)
      .map((result) => result.flight_id);
  }

  computeWorst(results: Response[]): string[] {
    let prices: number[] = results.map((result) => result.price);
    let highest = Math.max(...prices);
    return results
      .filter((result) => result.price === highest)
      .map((result) => result.flight_id);
  }

  ngOnInit(): void {
    this.activatedRoute.paramMap.subscribe((result) => {
      this.params =
        result.get('departure') +
        '/' +
        result.get('arrival') +
        '/' +
        result.get('date');
      this.resultsService.getResults(this.params).subscribe((flights) => {
        this.responses = flights;
        this.numResponses = flights.length;
        this.best_ids = this.computeBest(flights);
        this.worst_ids = this.computeWorst(flights);
      });
    });
  }
}
