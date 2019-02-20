import subprocess

print('RUNNING EXPERIMENT 1')

command = 'mpirun -hostfile hostfile -n 1 python3 mpi_hello.py'
arg = command.split()

for i in range(50):
    subprocess.run(arg)

print('FINISHED EXPERIMENT 1')
