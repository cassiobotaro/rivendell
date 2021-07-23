import typing

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AModel(BaseModel):
    name: str
    age: int


class OtherModel(BaseModel):
    name: str
    weird: int


class Response(BaseModel):
    msg: str


@app.post("/union")
def post_union(model: typing.Union[AModel, OtherModel]):
    return Response(msg=f"My name is {model.name} and my type {type(model)}")
