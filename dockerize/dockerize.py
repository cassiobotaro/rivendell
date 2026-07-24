"""
Dockerize

Dockerize will run 42 containers, being n (number of cores in the machine)
containers simultaneously, each one doing some task.
"""

import os
from concurrent.futures import ThreadPoolExecutor

import docker
from docker.errors import DockerException


def run_container(command):
    client = None
    try:
        client = docker.from_env()
        output = client.containers.run("alpine:latest", command, remove=True)
        print(output.decode("utf-8").strip())
    except DockerException as e:
        print(f"Failed to run {command}: {e}")
    finally:
        if client is not None:
            client.close()


if __name__ == "__main__":
    commands = [f"echo container {index}" for index in range(1, 43)]

    # Waiting on the docker daemon is I/O bound, so threads are enough here:
    # a process per worker would only add fork overhead.
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        # Consume the iterator so unexpected failures surface instead of
        # being swallowed by the lazy map.
        for _ in executor.map(run_container, commands):
            pass
