# Dockerize run

Dockerize will run 42 containers, being n (number of cores in the machine)
containers simultaneously, each one doing some task.

The work is I/O bound — every task just waits on the docker daemon — so it runs
on a `ThreadPoolExecutor` sized by `os.cpu_count()`.

## How to run

You should have [docker](https://docs.docker.com/engine/installation/) installed locally.

```bash
uv run dockerize.py
```
