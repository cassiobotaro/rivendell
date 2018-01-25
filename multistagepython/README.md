# Multi-stage builds with Python

How to optimize your python image using multi-stage build.

## How to run

### Step 1

Build the fist image, that uses python:3(debian) as base.

`docker build -t step1 -f Dockerfile.step1 .`

This generate a fat image, around 900 mb.

To check if it's running, type:

`docker run --rm step1`


### Step 2

Second image we change the base image, from debian to alpine.

Be careful when you do that because some apps have system dependencies.

`docker build -t step2 -f Dockerfile.step2 .`

Image reduce your size by half.

To check if it's running, type:

`docker run --rm step2`

### Step 3

Last step is to separate build and run process. We can use a machine with required compiler stuffs, to generate `.whl` and after copy it's files to another clean machine.

Again, be careful when you do that because some apps have system dependencies.

`docker build -t step3 -f Dockerfile.step3 .`

Image size reduce once more.

To check if it's running, type:

`docker run --rm step3`
