from mpi4py import MPI
import time
import subprocess

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
host = MPI.Get_processor_name()
payload_size = 32
size = comm.Get_size()
msg_num = 0
loss = 0
status_ = MPI.Status()

with open('results.csv', 'a') as csv:
    ColumnRow = 'rank, loss%, timestamp\n'
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
            if rank == 0:
                # print("Rank %s sending %d" % (rank, msg_num))
                data = bytes(payload_size)
                time_send = time.time()
                comm.send(data, dest=1, tag=msg_num)
                csv.write('1, %f, %f' % (loss, time_send))
                csv.write('\n')
                time_send = time.time()
                comm.send(data, dest=2, tag=msg_num)
                csv.write('2, %f, %f' % (loss, time_send))
                csv.write('\n')
                msg_num += 1
            elif rank != 0:
                data = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status_)
                if data is not None:
                    time_recv = time.time()
                    csv.write('%d, %f, %f' % (status_.source, loss, time_recv))
                    csv.write('\n')
                    msg_num += 1





