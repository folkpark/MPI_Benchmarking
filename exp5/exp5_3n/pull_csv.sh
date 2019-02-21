#!/usr/bin/env bash

scp mpi3:results.csv ./mpi3_recv.csv
scp mpi1:results.csv ./mpi1_send.csv
scp mpi2:results.csv ./mpi2_send.csv