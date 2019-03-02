#!/bin/bash
python3 ../send_scp.py ./zq_server.py ./ server
python3 ../send_scp.py ./zq_client.py ./ client1
python3 ../send_scp.py ./tc_setup.sh ./ server client1

HOSTS="server client1"
for HOSTNAME in ${HOSTS} ; do
    if [[ $HOSTNAME == *"server"* ]]
        then
            SCRIPT="./tc_setup.sh; chmod 700 zq_server.py; exit"
        else
            SCRIPT="./tc_setup.sh; chmod 700 zq_client.py; exit"
    fi
    echo Setting tc on $HOSTNAME
    ssh -o StrictHostKeyChecking=no $HOSTNAME "${SCRIPT}"
done

