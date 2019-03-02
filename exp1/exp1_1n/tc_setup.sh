#!/bin/bash
chmod 700 ./tc_setup.sh
sudo tc qdisc del dev eth0 root
sudo tc qdisc add dev eth0 handle 1: root htb default 11
sudo tc class add dev eth0 parent 1: classid 1:1 htb rate 1mbit burst 32kbit
sudo tc class add dev eth0 parent 1:1 classid 1:11 htb rate 7mbit ceil 7mbit
sudo tc qdisc add dev eth0 parent 1:11 handle 10: netem delay 14.844ms
sudo tc qdisc show dev eth0