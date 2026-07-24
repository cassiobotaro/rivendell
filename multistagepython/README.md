# Multi-stage builds with Python

How to optimize your python image using multi-stage build.

All steps install the same dependency (`pandas`) and run the same script, so the
only variable is how the image is built.

> Requires BuildKit (default since Docker 23) — steps 3 and 5 use `RUN --mount`.

## How to run

### Step 1

Build the first image, that uses `python:3.14` (debian) as base.

`docker build -t step1 -f Dockerfile.step1 .`

This generates a fat image, around 1.8 GB. The base image alone carries a full
build toolchain you will never use at runtime.

To check if it's running, type:

`docker run --rm step1`

### Step 2

Second image we change the base image, from debian to alpine.

`docker build -t step2 -f Dockerfile.step2 .`

Image size drops by a lot. Note that no compiler is installed: pandas publishes
`musllinux` wheels ([PEP 656](https://peps.python.org/pep-0656/)), so pip finds a
prebuilt wheel for alpine and nothing is compiled from source.

Still, be careful when you do that, because packages that don't ship musllinux
wheels will fall back to building from source, and that needs `build-base`.

To check if it's running, type:

`docker run --rm step2`

### Step 3

Now we separate build and run: a builder stage resolves and collects the `.whl`
files, and a clean final stage installs from them without touching the network.

`docker build -t step3 -f Dockerfile.step3 .`

The wheels are exposed to the final stage with `RUN --mount=type=bind,from=builder`
instead of `COPY`. This matters: `COPY` commits the wheels into a layer, and a
later `rm -rf` cannot shrink a layer that is already written — the image would
carry them forever. A bind mount makes them visible only during that `RUN`.

Image size ends up identical to step 2, because there was nothing to compile in
the first place.

To check if it's running, type:

`docker run --rm step3`

### Step 4

Let's create a minimal dockerfile using `python:3.14-slim` as base, a middle
ground between the full debian image and alpine.

`docker build -t step4 -f Dockerfile.step4 .`

To check if it's running, type:

`docker run --rm step4`

### Step 5

Same as step 4, but split into builder and runtime stages, again passing the
wheels through a bind mount.

`docker build -t step5 -f Dockerfile.step5 .`

It comes out ~10 MB below step 4. That gain is not from the multi-stage split —
the base layers are byte-for-byte identical — it comes from
`PYTHONDONTWRITEBYTECODE=1`, which keeps pip from writing `.pyc` files into the
image.

To check if it's running, type:

`docker run --rm step5`

### Conclusion

```bash
docker images --filter=reference='step*' --format='{{.Repository}}:{{.Tag}} - {{.Size}}' | sort
step1:latest - 1.82GB
step2:latest - 293MB
step3:latest - 293MB
step4:latest - 385MB
step5:latest - 371MB
```

Most of the win comes from picking the right base image, not from multi-stage.
Going from `python:3.14` to `python:3.14-alpine` cuts 84% of the size; every
technique after that moves the number by single-digit percentages.

Multi-stage pays off when the build genuinely needs tooling the runtime doesn't —
a compiler, headers, a private index token. Since Python wheels cover that case
for most packages today, the split is often size-neutral: step 3 ties with step 2.
It is not free either, so reach for it when there is something to leave behind.

Alpine is the smallest here and, unlike a few years ago, it no longer forces a
source build for a package like pandas. The old caveat still holds for anything
without musllinux wheels: check before switching, or you trade image size for
build time.

Measured on linux/amd64 with Docker 29.6.2, `python:3.14`, pandas 3.0.5.
