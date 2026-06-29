import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseUrl =
  "https://supreme-space-barnacle-qj477697rrjfxqg4-8000.app.github.dev";

  constructor(
    private http: HttpClient
  ) {}

  summary() {

    return this.http.get(
      this.baseUrl + "/summary"
    );

  }

  review() {

    return this.http.get(
      this.baseUrl + "/review"
    );

  }

  chat(request:any) {

    return this.http.post(
      this.baseUrl + "/chat",
      request
    );

  }

  spring() {

    return this.http.get(
      this.baseUrl + "/generate/spring"
    );

  }

  angular() {

    return this.http.get(
      this.baseUrl + "/generate/angular"
    );

  }

}