import { IsNotEmpty, Max, Min } from 'class-validator';

export class CreateStrangeCatDto {
  @IsNotEmpty()
  name: string;

  @Min(1)
  @Max(5)
  strange: number;

  type: string;
}
