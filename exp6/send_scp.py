import subprocess
from time import sleep
from sys import argv

if __name__ == '__main__':

    file_str = argv[1]
    dest_loc_str = argv[2]
    host_list = []

    i = 3
    while i < len(argv):

        if argv[i] == 'all':
            host_list = ['mpi1', 'mpi2', 'mpi3', 'mpi4', 'mpi5', 'mpi6']
        else:
            host_list.append(argv[i])
        i += 1

    for i in range(len(host_list)):
        command = ['scp', file_str]
        if dest_loc_str != './':
            host = host_list[i] + ':' + dest_loc_str
        else:
            host = host_list[i] + ':'
        command.append(host)
        subprocess.run(command)
        sleep(1)



