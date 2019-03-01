#!/usr/bin/python3
import subprocess

print('RUNNING EXPERIMENT 3 with 2 nodes')

command = 'mpirun -hostfile hostfile -n 2 python3 mpi_ch_size.py'
arg = command.split()

for i in range(2):
    subprocess.run(arg)

print('FINISHED EXPERIMENT 3 with 2 nodes')

