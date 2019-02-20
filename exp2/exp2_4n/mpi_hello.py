from mpi4py import MPI

comm = MPI.COMM_WORLD
host = MPI.Get_processor_name()
print("Hello! Host %s rank %d from %d running in total..." % (host, comm.rank, comm.size))

