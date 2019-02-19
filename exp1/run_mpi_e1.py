import subprocess

command = 'mpirun -hostfile hostfile -n 1 python3 mpi_1.py'
arg = command.split()

for i in range(50):
    subprocess.run(arg)

