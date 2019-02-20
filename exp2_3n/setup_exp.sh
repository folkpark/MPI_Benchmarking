#!/bin/bash

python3 /Users/justinelias/Desktop/college_courses/csci566/pa2/MPI_Benchmarking/send_scp.py ./hostfile ./ mpi1
python3 /Users/justinelias/Desktop/college_courses/csci566/pa2/MPI_Benchmarking/send_scp.py ./run.py ./ mpi1
python3 /Users/justinelias/Desktop/college_courses/csci566/pa2/MPI_Benchmarking/send_scp.py ./mpi_hello.py ./ all