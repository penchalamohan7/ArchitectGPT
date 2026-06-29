import {
  Component,
  inject,
  ChangeDetectorRef
} from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from './services/api.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {

  api = inject(ApiService);
  cdr = inject(ChangeDetectorRef);

  summary: any = {
    title: '',
    version: '',
    endpointCount: 0
  };

  constructor() {
    this.loadSummary();
  }

  loadSummary() {

    this.api.summary().subscribe((res: any) => {

      this.summary = res;

      this.cdr.detectChanges();

    });

  }

}