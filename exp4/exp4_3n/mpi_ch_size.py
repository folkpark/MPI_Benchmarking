from mpi4py import MPI
import time
import os

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
host = MPI.Get_processor_name()
payload_size = 32
size = comm.Get_size()
msg_num = 0
status_ = MPI.Status()
has_run = False

if os.path.isfile('./results.csv') is False:
    with open('results.csv', 'a') as csv:
        ColumnRow = 'rank, msg_num, timestamp\n'
        csv.write(ColumnRow)
while msg_num < 100:
    with open('results.csv', 'a') as csv:
        if rank != 0:
            # print("Rank %s sending %d" % (rank, msg_num))
            data = bytes(payload_size)
            time_send = time.time()
            comm.send(data, dest=0, tag=msg_num)
            csv.write('%s, %s, %f' % (rank, msg_num, time_send))
            csv.write('\n')
            msg_num += 1
        elif rank == 0:
            data = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status_)
            if data is not None:
                time_recv = time.time()
                csv.write('%d, %d, %f' % (status_.source, status_.tag, time_recv))
                csv.write('\n')
                msg_num += 1




