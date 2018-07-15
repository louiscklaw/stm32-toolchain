#!/usr/bin/env python
# init_py_dont_write_bytecode

#init_boilerplate

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.project import *


import multiprocessing
total_cpu_threads = multiprocessing.cpu_count()

CWD = os.path.dirname(__file__)
PROJ_HOME=[CWD, '/home/logic/docker_tmp']

def threaded_local(command):
    local(command, capture=True)


def helloworld():
    # p.map(threaded_local,['id'])
    run('mkdir -p {}'.format(PROJ_HOME[1]))
    put(PROJ_HOME[0],PROJ_HOME[1])
    # with cd(PROJ_HOME[1]+'/stm32-toolchain'):
    #     run('docker build .')
