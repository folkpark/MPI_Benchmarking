#!/bin/bash
python3 ../send_scp.py ./hostfile ./ mpi1
python3 ../send_scp.py ./run.py ./ mpi1
python3 ../send_scp.py ./mpi_ch_size.py ./ mpi1 mpi2
python3 ../send_scp.py ./tc_setup.sh ./ mpi1 mpi2

HOSTS="mpi1 mpi2 "
SCRIPT="./tc_setup.sh ; rm *.csv; exit"
for HOSTNAME in ${HOSTS} ; do
    echo Setting tc on $HOSTNAME
    ssh -o StrictHostKeyChecking=no $HOSTNAME "${SCRIPT}"
done

