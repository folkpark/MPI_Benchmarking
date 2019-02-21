from mpi4py import MPI
import time
from sys import argv

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
host = MPI.Get_processor_name()
payload_size = 32
size = comm.Get_size()
msg_tot = int(float(argv[1]))
file_name = 'rank_' + str(rank) + '.csv'
sent_time = {}
msg_num = 0
beg = 0.0
delta = 0.0

if rank == 1:
    data = bytes(payload_size)
    beg = time.time()
    while True:
        if msg_tot in sent_time:
            sent_time[msg_tot][msg_num] = time.time()
        else:
            sent_time[msg_tot] = {msg_num: time.time()}
        comm.send(data, dest=0, tag=msg_num)
        msg_num += 1
        if msg_tot == msg_num:
            break
    end = time.time()
    delta = end - beg

    with open(file_name, 'a') as csv:
        # sent_time[msg_tot] = {msg_num: time.time()}
        for k1, v1 in sent_time.items():
            for k2, v2 in v1.items():
                csv.write('%d, %d, %d, %f' % (rank, k1, k2, v2))
                csv.write('\n')

elif rank == 2:
    with open(file_name, 'a') as csv:

        while True:
            data = comm.recv(source=0, tag=msg_num)
            if data is not None:
                time_recv = time.time()
                csv.write('%d, %d, %d, %f' % (rank, msg_tot, msg_num, time_recv))
                csv.write('\n')
                msg_num += 1
            if msg_tot == msg_num:
                break
elif rank == 0:
    while True:
        data = comm.recv(source=1, tag=msg_num)
        if data is not None:
            comm.send(data, dest=2, tag=msg_num)
            msg_num += 1
        if msg_tot == msg_num:
            break
if rank == 1:
    print('%s sent %d in %f sec' % (rank, msg_num, delta))
if rank == 2:
    print('%s recv %d' % (rank, msg_num))
