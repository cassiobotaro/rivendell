"""
Dockerize

Dockerize will run 42 containers,beign n(number of cores in machine)
containers simutaneously, each one doing some task.
"""

import os
from multiprocessing import Pool

import docker


def run_container(command):
    client = docker.from_env()
    try:
        output = client.containers.run("alpine:latest", command, remove=True)
        print(output.decode("utf-8").strip())
    except Exception as e:
        print(f"Erro ao executar {command}: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    commands = [f"echo container {index}" for index in range(1, 43)]

    with Pool(os.cpu_count()) as p:
        p.map(run_container, commands)
