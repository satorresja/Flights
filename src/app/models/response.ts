import { Transport } from './transport';
export class Response {

  departureStation: string;
  arrivalStation: string;
  departureDate: string;
  transport: Transport[];
  prize: number;
  currency: string;
}
