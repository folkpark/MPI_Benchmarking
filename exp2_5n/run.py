import subprocess

print('RUNNING EXPERIMENT 2 with 5 nodes')

command = 'mpirun -hostfile hostfile -n 5 python3 mpi_hello.py'
arg = command.split()

for i in range(50):
    subprocess.run(arg)

print('FINISHED EXPERIMENT 2 with 5 nodes')

