import { IsInt, IsNotEmpty } from 'class-validator';

export class CreateCatDto {
  @IsNotEmpty()
  name: string;

  @IsInt()
  age: number;

  type: string;
}
