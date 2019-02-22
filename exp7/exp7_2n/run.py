#!/usr/bin/python3
import subprocess

print('RUNNING EXPERIMENT 7 with 2 nodes')
i = 0
while i < 5:
    command = 'mpirun -hostfile hostfile -n 2 python3 mpi_ch_size.py'
    arg = command.split()
    subprocess.run(arg)
    i += 1
print('FINISHED EXPERIMENT 7 with 2 nodes')

