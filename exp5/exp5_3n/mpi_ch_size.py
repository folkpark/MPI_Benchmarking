from mpi4py import MPI
import time
import subprocess

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
host = MPI.Get_processor_name()
payload_size = 32
loss = 0
size = comm.Get_size()


file_name = 'rank_' + str(rank) + '.csv'

with open(file_name, 'w') as csv:
    ColumnRow = 'rank, msg_num, loss%, timestamp\n'
    csv.write(ColumnRow)

    while loss < 2.0:
        msg_num = 0
        loss += 0.2
        print("%s at %f loss" % (host, loss))
        loss_per = loss/size
        command = './tc_setup.sh ' + str(loss_per)
        arg = command.split()
        subprocess.run(arg)
        while msg_num < 100:
            if rank != 0:
                data = bytes(payload_size)
                time_send = time.time()
                comm.send(data, dest=0, tag=msg_num)
                csv.write('%d, %d %s, %f' % (rank, msg_num, loss, time_send))
                csv.write('\n')
                msg_num += 1
            elif rank == 0:
                data = comm.recv(source=1, tag=msg_num)
                if data is not None:
                    time_recv = time.time()
                    csv.write('%d, %d, %s, %f' % (rank, msg_num, loss, time_recv))
                    csv.write('\n')
                    msg_num += 1

    print('%s ended' % host)

