#!/bin/bash
python3 ../send_scp.py ./hostfile ./ mpi1
python3 ../send_scp.py ./run.py ./ mpi1
python3 ../send_scp.py ./mpi_hello.py ./ all
python3 ../send_scp.py ./tc_setup.sh ./ all

#!/bin/bash
HOSTS="mpi1 mpi2 mpi3 mpi4 mpi5 mpi6"
SCRIPT="./tc_setup.sh; exit"
for HOSTNAME in ${HOSTS} ; do
    echo Setting tc on $HOSTNAME
    ssh -o StrictHostKeyChecking=no $HOSTNAME "${SCRIPT}"

done

