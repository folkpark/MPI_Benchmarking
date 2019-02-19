#!/bin/bash

tc qdisc add dev eth0 handle 1: root htb default 11
tc class add dev eth0 parent 1: classid 1:1 htb rate 10Mbit ceil 10Mbit
tc class add dev eth0 parent 1:1 classid 1:11 htb rate 10Mbit ceil 10Mbit
tc qdisc add dev eth0 parent 1:11 handle 10: netem delay 15ms
