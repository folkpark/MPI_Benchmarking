#!/usr/bin/python3
import subprocess

print('RUNNING EXPERIMENT 3 with 3 nodes')

command = 'mpirun -hostfile hostfile -n 3 python3 mpi_ch_size.py'
arg = command.split()

subprocess.run(arg)

print('FINISHED EXPERIMENT 3 with 3 nodes')

