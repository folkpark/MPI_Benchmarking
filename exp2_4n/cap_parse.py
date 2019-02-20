import pyshark
from collections import defaultdict
from statistics import mean

cap = pyshark.FileCapture('./mpi_exp2_4n_2ndTest.pcapng')
syn_list = []
syn_ack_dict = defaultdict(list)
ack_dict = defaultdict(list)
fin_ack_dict = defaultdict(list)
conn_time = []

# TODO: setup discard of retrans SYN or SYN/ACK packets.
# Probably by only allowing first relative time per stream
for pkt in cap:

    if 'TCP' in pkt:
        if pkt.tcp.flags == '0x00000002':                   # SYN packet, 1 per stream
            syn_list.append(pkt)
        if pkt.tcp.flags == '0x00000012':                   # SYN/ACK packet, 1 per stream
            syn_ack_dict[pkt.tcp.stream].append(pkt)
        if pkt.tcp.flags == '0x00000010':                   # 1st ACK packet in stream
            if pkt.tcp.seq == '1' and pkt.tcp.ack == '1':
                ack_dict[pkt.tcp.stream].append(pkt)
        if pkt.tcp.flags == '0x00000011':                   # Fin/ACK packet, 2 per stream
            fin_ack_dict[pkt.tcp.stream].append(pkt)

for pkt in syn_list:
    ack = ack_dict[pkt.tcp.stream].pop()

    syn_time = float(pkt.tcp.time_relative)
    ack_time = float(ack.tcp.time_relative)

    time_delta = ack_time - syn_time
    conn_time.append(time_delta)

min_value = min(conn_time)*1000
max_value = max(conn_time)*1000
mean_value = mean(conn_time)*1000
print(' Min: %fms\n Mean: %fms\n Max: %fms' % (min_value, mean_value, max_value))





