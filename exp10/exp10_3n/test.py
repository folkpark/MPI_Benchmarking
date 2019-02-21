import time
from sys import argv

payload_size = 32
msg_tot = int(float(256))
file_name = 'rank_' + str('TEST') + '.csv'
sent_time = {}
msg_num = 0
delta = 0.0
rank = 1

if rank == 1:
    data = bytes(payload_size)
    beg = time.time()
    while True:
        if msg_tot in sent_time:

            sent_time[msg_tot][msg_num] = time.time()
        else:
            sent_time[msg_tot] = {msg_num: time.time()}
        msg_num += 1
        if msg_tot == msg_num:
            break
    end = time.time()
    delta = end - beg

    with open(file_name, 'a') as csv:
        # sent_time[msg_tot] = {msg_num: time.time()}
        for k1, v1 in sent_time.items():
            for k2 in v1.keys():
                for v2 in v1.values():
                    csv.write('%d, %d, %d, %f' % (rank, k1, k2, v2))
                    csv.write('\n')
