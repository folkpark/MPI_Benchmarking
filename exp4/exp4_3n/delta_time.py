import csv
from statistics import mean

# rank {msg_num:time}
rank1 = {}
rank2 = {}
rank3 = {}
delta = []
delta1 = []
ntp_shift = {}
with open('./mpi1.csv') as mpi1, open('./mpi2.csv') as mpi2, open('./mpi3.csv') as mpi3, open('./mpi4.csv') as mpi4, open('/Users/justinelias/Desktop/college_courses/csci566/pa2/MPI_Benchmarking/ntp_shifts.csv') as shift:
    reader1 = csv.reader(mpi1)
    reader2 = csv.reader(mpi2)
    reader3 = csv.reader(mpi3)
    reader4 = csv.reader(mpi4)
    shift_reader = csv.reader(shift)

    trash = next(shift_reader)
    for row in shift_reader:
        ntp_shift[row[0]] = float(row[1])

    trash = next(reader1)
    for row in reader1:
        if row[0] == '1':
            rank1[int(row[1])] = float(row[2]) + ntp_shift['mpi1']
        if row[0] == '2':
            rank2[int(row[1])] = float(row[2]) + ntp_shift['mpi1']
        if row[0] == '3':
            rank3[int(row[1])] = float(row[2]) + ntp_shift['mpi1']
    trash = next(reader2)

    i = 0
    for row in reader2:
        if i < len(rank1):
            delta.append(float(row[2]) + ntp_shift['mpi2'] - rank1[i])
            i += 1
        else:
            break

    i = 0
    trash = next(reader3)
    for row in reader3:
        if i < len(rank2):
            delta.append(float(row[2]) + ntp_shift['mpi3'] - rank2[i])
            i += 1
        else:
            break

    i = 0
    trash = next(reader4)
    for row in reader4:
        if i < len(rank3):
            delta.append(float(row[2]) + ntp_shift['mpi4'] - rank3[i])
            i += 1
        else:
            break

    print('min_value1 = %f' % (min(delta) * 1000))
    print('mean_value1 = %f' % (mean(delta) * 1000))
    print('max_value1 = %f\n' % (max(delta) * 1000))

