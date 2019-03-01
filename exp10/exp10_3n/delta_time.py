import csv
from statistics import mean

sender = {}
recvr = {}
deltas = []
with open('./send.csv') as f, open('./recv.csv') as g:

    readerf = csv.DictReader(f)
    readerg = csv.DictReader(g)

    for row in readerf:
        print(row['rate'])
        if row['rate'] in sender:
            sender[row['rate']][row['msg_num']] = row['timestamp']
        else:
            sender[row['rate']] = {row['msg_num']: row['timestamp']}

    for row in readerg:
        if row['rate'] in recvr:
            recvr[row['rate']][row['msg_num']] = row['timestamp']
        else:
            recvr[row['rate']] = {row['msg_num']: row['timestamp']}

    for rate in sender:
        for msg, time in rate.items():
            deltas.append(recvr[rate][msg] - time)

    min_value = min(deltas) * 1000
    max_value = max(deltas) * 1000
    mean_value = mean(deltas) * 1000
