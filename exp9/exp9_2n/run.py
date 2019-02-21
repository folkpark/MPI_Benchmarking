#!/usr/bin/python3
import subprocess
payload_size = 1
print('RUNNING EXPERIMENT 3 with 2 nodes')

while payload_size <= 1048576:
    command = 'mpirun -hostfile hostfile -n 2 python3 mpi_ch_size.py ' + str(payload_size)
    arg = command.split()
    subprocess.run(arg)
    payload_size = payload_size * 2
print('FINISHED EXPERIMENT 3 with 2 nodes')

