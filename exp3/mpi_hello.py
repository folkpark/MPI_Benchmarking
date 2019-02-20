from mpi4py import MPI
import ntplib

comm = MPI.COMM_WORLD
host = MPI.Get_processor_name()
print("Hello! Host %s rank %d from %d running in total..." % (host, comm.rank, comm.size))


ntplib.system_to_ntp_time()