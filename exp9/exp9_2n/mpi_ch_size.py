from mpi4py import MPI
import time
from sys import stdout, argv
import tempfile

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
host = MPI.Get_processor_name()
payload_size = int(argv[1])

with tempfile.TemporaryFile() as dummy:
    if rank == 1:
        data = dummy.write(b'0' * payload_size)
        time_send = time.time()
        comm.send(data, dest=0, tag=payload_size)
    elif rank == 0:
        stdout.write('*')
        data = comm.recv(source=1, tag=payload_size)
        if data is not None:
            time_recv = time.time()
