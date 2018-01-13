'''
Dockerize

Dockerize will run 42 containers,beign n(number of cores in machine)
containers simutaneously, each one doing some task.
'''
import os
from multiprocessing import Pool

import docker


def run_container(command):
    # instantiate a client using default socket or enviroment variable.
    client = docker.from_env()
    # run some command using alpine:latest and then remove the container
    output = client.containers.run('alpine:latest', command, remove=True)
    # print standard output from container
    print(output.decode('utf-8'))


# list of commands to run
commands = [f'echo container {index}' for index in range(1, 43)]

# do a process pool and invoke `run_container` with each command in commands
# list
with Pool(os.cpu_count()) as p:
    p.map(run_container, commands)
