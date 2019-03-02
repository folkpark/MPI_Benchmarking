import subprocess

print('RUNNING EXPERIMENT 1')

command = 'python3 zq_server.py'
arg = command.split()

subprocess.run(arg)

print('FINISHED EXPERIMENT 1')
