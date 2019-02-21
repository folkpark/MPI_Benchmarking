#!/usr/bin/python3
import subprocess
from sys import stdout

print('RUNNING EXPERIMENT 4 with 3 nodes')


command = 'mpirun -hostfile hostfile -n 4 python3 mpi_ch_size.py'
arg = command.split()

for i in range(50):
    stdout.write('.')
    subprocess.run(arg)

stdout.flush()
print('FINISHED EXPERIMENT 4 with 3 nodes')

