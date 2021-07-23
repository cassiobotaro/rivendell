import {
  Controller,
  Get,
  Post,
  Body,
  Patch,
  Param,
  Delete,
  Injectable,
  PipeTransform,
  BadRequestException,
} from '@nestjs/common';
import { ApiBody, ApiExtraModels, getSchemaPath } from '@nestjs/swagger';
import { plainToClass } from 'class-transformer';
import { validate } from 'class-validator';
import { CatsService } from './cats.service';
import { CreateCatDto } from './dto/create-cat.dto';
import { CreateStrangeCatDto } from './dto/create-strange-cat.dto';
import { UpdateCatDto } from './dto/update-cat.dto';

@Injectable()
export class ValidationPipe implements PipeTransform<any> {
  async transform(value: any) {
    let kls = null;
    switch (value.type) {
      case 'regular':
        kls = CreateCatDto;
        break;
      case 'strange':
        kls = CreateStrangeCatDto;
        break;
      default:
        throw new BadRequestException('Validation failed');
    }
    const object = plainToClass(kls, value);
    const errors = await validate(object);
    if (errors.length > 0) {
      throw new BadRequestException(errors);
    }
    return object;
  }
}

@Controller('cats')
export class CatsController {
  constructor(private readonly catsService: CatsService) {}

  @ApiBody({
    schema: {
      oneOf: [
        { $ref: getSchemaPath(CreateCatDto) },
        { $ref: getSchemaPath(CreateStrangeCatDto) },
      ],
    },
  })
  @ApiExtraModels(CreateCatDto, CreateStrangeCatDto)
  @Post()
  create(
    @Body(new ValidationPipe()) someCat: CreateCatDto | CreateStrangeCatDto,
  ) {
    if (someCat instanceof CreateStrangeCatDto) {
      return `${someCat.name} Strange: ${someCat.strange}`;
    }
    return `${someCat.name} - CreateCatDto`;
  }

  @Get()
  findAll() {
    return this.catsService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.catsService.findOne(+id);
  }

  @Patch(':id')
  update(@Param('id') id: string, @Body() updateCatDto: UpdateCatDto) {
    return this.catsService.update(+id, updateCatDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.catsService.remove(+id);
  }
}
