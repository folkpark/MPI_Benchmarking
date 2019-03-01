import csv
from statistics import mean


rank1 = []
rank2 = []
delta = []
with open('./mpi1.csv') as mpi1, open('./mpi2.csv') as mpi2, open('./mpi3.csv') as mpi3:
    reader1 = csv.reader(mpi1)
    reader2 = csv.reader(mpi2)
    reader3 = csv.reader(mpi3)

    trash = next(reader1)
    for row in reader1:
        if row[0] == '1':
            rank1.insert(int(row[1]), float(row[2]))
        if row[0] == '2':
            rank2.insert(int(row[1]), float(row[2]))
    trash = next(reader2)

    i = 0
    for row in reader2:
        if i < len(rank1):
            delta.append(rank1[i] - float(row[2]))
            i += 1
        else:
            break

    i = 0
    trash = next(reader3)
    for row in reader3:
        if i < len(rank2):
            delta.append(rank2[i] - float(row[2]))
            i += 1
        else:
            break

    print('min_value1 = %f' % (min(delta) * 1000))
    print('mean_value1 = %f' % (mean(delta) * 1000))
    print('max_value1 = %f' % (max(delta) * 1000))


