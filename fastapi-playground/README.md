# FastAPI Playground 🕹️

## Requirements

Use poetry to install dependencies:

    $ pip install poetry
    $ poetry install

## How to run

    $ poetry run uvicorn main:app --reload

**Q: How to receive different types of payload?**

We can use `typing.Union` as you can see in `/union` endpoint.
NOTE: `typing.Union` is not supported in Python 3.5 and can be replaced by `|` in Python 3.10.
The OpenAPI specification is correctly created using the `anyOf` element. A detail is in the validation of the fields, if it does not fit in any of the structures, the lack of all fields of all structures will be reported, including those that are repeated.