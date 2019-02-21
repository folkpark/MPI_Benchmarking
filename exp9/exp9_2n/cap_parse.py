import pyshark
import tempfile

cap = pyshark.FileCapture('./mpi_exp9_2n.pcapng')

payload_size = 1
streams = {}

with open('stream_len.csv', 'w') as csv:
    ColumnRow = 'payload_size, stream_size, overhead\n'
    csv.write(ColumnRow)

    for pkt in cap:
        if 'TCP' in pkt:
            if pkt.ip.src == '172.31.82.249':
                if int(pkt.tcp.stream) in streams.keys():
                    streams[int(pkt.tcp.stream)].append(int(pkt.length))
                else:
                    streams[int(pkt.tcp.stream)] = [int(pkt.length)]

    for stream, values in streams.items():
        length_stream = 0
        for length in values:
            length_stream += length
        if length_stream > 530:
            overhead = length_stream - payload_size
            csv.write('%d, %d, %d' % (payload_size, length_stream, overhead))
            csv.write('\n')
            payload_size = payload_size * 2

