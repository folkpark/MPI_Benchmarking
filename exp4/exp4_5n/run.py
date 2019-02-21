#!/usr/bin/python3
import subprocess
from sys import stdout

print('RUNNING EXPERIMENT 4 with 5 nodes')


command = 'mpirun -hostfile hostfile -n 6 python3 mpi_ch_size.py'
arg = command.split()

subprocess.run(arg)

print('FINISHED EXPERIMENT 4 with 5 nodes')

