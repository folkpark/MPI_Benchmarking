from mpi4py import MPI
import subprocess

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
host = MPI.Get_processor_name()
payload_size = 32
loss = 1.6
size = comm.Get_size()


msg_num = 0
print("At %f loss" % loss)
loss_per = loss / size
command = './tc_setup.sh ' + str(loss_per)
arg = command.split()
subprocess.run(arg)
while msg_num < 100:
    if rank != 0:
        data = bytes(payload_size)
        comm.send(data, dest=0, tag=msg_num)
        msg_num += 1
    elif rank == 0:
        data = comm.recv(source=1, tag=msg_num)
        if data is not None:
            msg_num += 1


print('ended')

