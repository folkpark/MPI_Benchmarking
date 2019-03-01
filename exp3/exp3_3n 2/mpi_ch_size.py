from mpi4py import MPI
import time
from sys import stdout

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
host = MPI.Get_processor_name()
payload_size = 1
size = comm.Get_size()
file_name = ''

print('Rank %s of %s' % (rank, size))

if rank == 1:
    file_name = 'send.csv'
elif rank == 2:
    file_name = 'recv.csv'
with open(file_name, 'w') as csv:
    ColumnRow = 'size, timestamp\n'
    csv.write(ColumnRow)

    while payload_size <= 1048576:
        if rank == 1:
            data = bytes(payload_size)
            time_send = time.time()
            comm.send(data, dest=0, tag=payload_size)
            csv.write('%s, %f' % (payload_size, time_send))
            csv.write('\n')
            payload_size = payload_size * 2
        elif rank == 2:
            data = comm.recv(source=0, tag=payload_size)
            if data is not None:
                time_recv = time.time()
                csv.write('%s, %f' % (payload_size, time_recv))
                csv.write('\n')
                payload_size = payload_size * 2
        elif rank == 0:
            data = comm.recv(source=1, tag=payload_size)
            if data is not None:
                comm.send(data, dest=2, tag=payload_size)
                payload_size = payload_size * 2

