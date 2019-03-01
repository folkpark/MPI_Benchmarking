import csv
from statistics import mean
from decimal import *

# rank {msg_num:time}
rank1 = {}
delta = {}
ntp_shift = {}
with open('./mpi1.csv') as mpi1, open('./mpi2.csv') as mpi2, \
        open('/Users/justinelias/Desktop/college_courses/csci566/pa2/MPI_Benchmarking/ntp_shifts.csv') as shift:
    reader1 = csv.reader(mpi1)
    reader2 = csv.reader(mpi2)
    shift_reader = csv.reader(shift)

    trash = next(shift_reader)
    for row in shift_reader:
        ntp_shift[row[0]] = Decimal(row[1])

    trash = next(reader1)
    for row in reader1:
        if row[0] == '1' and round(Decimal(row[2]), 1) != 2.2:
            if round(Decimal(row[2]), 1) in rank1:
                if int(row[1]) in rank1[round(Decimal(row[2]), 1)]:
                    rank1[round(Decimal(row[2]), 1)][int(row[1])] = (Decimal(row[3]) + ntp_shift['mpi1'])
                else:
                    rank1[round(Decimal(row[2]), 1)][int(row[1])] = Decimal(row[3]) + ntp_shift['mpi1']
            else:
                rank1[round(Decimal(row[2]), 1)] = {int(row[1]): Decimal(row[3]) + ntp_shift['mpi1']}

    trash = next(reader2)

    for row in reader2:
        i = 0
        if round(float(row[2]), 1) == 2.2:
            break
        while i < len(rank1[round(Decimal(row[2]), 1)]):
            temp = ((Decimal(row[3]) + ntp_shift['mpi2']) - rank1[round(Decimal(row[2]), 1)][i])
            if temp < 0:
                pass
            elif round(Decimal(row[2]), 1) in delta:
                delta[round(Decimal(row[2]), 1)].append(abs(((Decimal(row[3]) + ntp_shift['mpi2']) - rank1[round(Decimal(row[2]), 1)][i])))
            else:
                delta[round(Decimal(row[2]), 1)] = [abs(((Decimal(row[3]) + ntp_shift['mpi2']) - rank1[round(Decimal(row[2]), 1)][i]))]
            i += 1

    with open('delta_output.csv', 'w') as out:
        out.write('loss,min,mean,max\n')
        for key, value in delta.items():
            min_value = (min(value) * 1000)
            mean_value = (mean(value) * 1000)
            max_value = (max(value) * 1000)
            out.write('%s,%f,%f,%f\n' % (key, min_value, mean_value, max_value))
            print('min_value %s = %f' % (key, (min(value) * 1000)))
            print('mean_value1 %s = %f' % (key, (mean(value) * 1000)))
            print('max_value1 % s = %f\n' % (key, (max(value) * 1000)))

