import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { HomeService } from './home.service';
import { formatDate } from '@angular/common';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  departs: string[] = ['Bogota', 'Medellin', 'Manizales'];
  destinations: string[] = ['Medellin', 'Bogota', 'Manizales'];
  dataForm: FormGroup;
  error: string = '';
  today: string = '2020-09-27';

  constructor(
    private fb: FormBuilder,
    private flightService: HomeService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.dataForm = this.fb.group({
      departCity: ['', [Validators.required]],
      destinationCity: '',
      date: '',
    });
  }

  validateInput(): boolean {
    let date = this.dataForm.get('date').value;
    let departCity = this.dataForm.get('departCity').value;
    let destinationCity = this.dataForm.get('destinationCity').value;

    if (!departCity) {
      this.error = 'You must enter depart city !';
      return false;
    }

    if (!destinationCity) {
      this.error = 'You must enter destination city !';
      return false;
    }

    if (!date) {
      this.error = 'You must enter depart date !';
      return false;
    }

    if (departCity === destinationCity) {
      this.error = 'Depart city cannot be equal to destination city !';
      return false;
    }

    return true;
  }

  onSubmit() {
    if (!this.validateInput()) {
      return;
    }

    let date = this.dataForm.get('date').value;
    let departCity = this.dataForm.get('departCity').value;
    let destinationCity = this.dataForm.get('destinationCity').value;

    const formattedDate = formatDate(date, 'yyyy-MM-dd', 'en-us');
    this.router.navigateByUrl(
      '/results/' + departCity + '/' + destinationCity + '/' + formattedDate
    );
  }
}
