from mpi4py import MPI
import time
from sys import stdout

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
host = MPI.Get_processor_name()
payload_size = 1
size = comm.Get_size()


file_name = 'rank_' + str(rank) + '.csv'

with open(file_name, 'w') as csv:
    ColumnRow = 'rank, msg_num, payload_size, timestamp\n'
    csv.write(ColumnRow)

    while payload_size <= 1048576:
        msg_num = 0
        while msg_num < 100:
            if rank == 1:
                data = bytes(payload_size)
                time_send = time.time()
                comm.send(data, dest=0, tag=msg_num)
                csv.write('%d, %d, %s, %f' % (rank, msg_num, payload_size, time_send))
                csv.write('\n')
                msg_num += 1
            elif rank == 0:
                stdout.write('*')
                data = comm.recv(source=1, tag=msg_num)
                if data is not None:
                    time_recv = time.time()
                    csv.write('%d, %d, %s, %f' % (rank, msg_num, payload_size, time_recv))
                    csv.write('\n')
                    msg_num += 1

        payload_size = payload_size * 2

