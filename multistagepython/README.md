# Multi-stage builds with Python

How to optimize your python image using multi-stage build.

## How to run

### Step 1

Build the fist image, that uses python:3(debian) as base.

`docker build -t step1 -f Dockerfile.step1 .`

This generate a fat image, around 1 GB.

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

### Step 4

Let's create a minimal dockerfile using `python:3-slim` as base.
Alpine don't have whells and it is a problem, then we will use slim images to reduce image size.


`docker build -t step4 -f Dockerfile.step4 .`

To check if it's running, type:

`docker run --rm step4`

### Step 5

Exactly like step4 but we use multi stage building to cache our dependencies and improve build speed.

`docker build -t step5 -f Dockerfile.step5 .`

To check if it's running, type:

`docker run --rm step5`


### Conclusion

Multi stage build can help when you have to compile some dependencies, but as python have [wheels](https://pythonwheels.com/), maybe it's not the best choice for the language.

Alpine is a tiny image, but don't support wheels and also have problems with system dependencies. Build takes a lot of time.

```bash
docker images --filter=reference='step*' --format='{{.Repository}}:{{.Tag}} - {{.Size}}' | sort
step1:latest - 1.04GB
step2:latest - 333MB
step3:latest - 192MB
step4:latest - 247MB
step5:latest - 259MB
```

Surprisingly, multi-stage build (step 5) is greater than minimum build with `python:3-slim` as base (step 4).