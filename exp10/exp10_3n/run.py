#!/usr/bin/python3
import subprocess

print('RUNNING EXPERIMENT 3 with 3 nodes')

msg_tot = 256
while True:
    command = 'mpirun -hostfile hostfile -n 3 python3 mpi_ch_size.py ' + str(msg_tot)
    arg = command.split()
    subprocess.run(arg)
    if msg_tot == 1:
        break
    msg_tot = msg_tot/2
print('FINISHED EXPERIMENT 3 with 3 nodes')

