import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { HomeService } from './home.service';
import { formatDate } from '@angular/common';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  origins: string[] = ['BOGOTA', 'MEDELLIN', 'MANIZALES'];
  destinations: string[]  = ['MEDELLIN', 'BOGOTA', 'MANIZALES'];
  dataForm: FormGroup;

  constructor(private fb: FormBuilder, private flightService: HomeService, private router: Router) { }

  ngOnInit(): void {
    this.dataForm = this.fb.group({
      originCity: ['', [Validators.required]],
      destinationCity: '',
      date: ''
    });
  }

  onSubmit() {
    const formattedDate = formatDate(this.dataForm.get('date').value, 'yyyy-MM-dd', 'en-us');
    console.log('/results/'+this.dataForm.get('originCity').value+'/'+this.dataForm.get('destinationCity').value+'/'+formattedDate);
    this.router.navigateByUrl('/results/'+this.dataForm.get('originCity').value+'/'+this.dataForm.get('destinationCity').value+'/'+formattedDate);
  }
}
