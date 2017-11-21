import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.connect(('127.0.0.1', 8333))

while True:
    mes = raw_input('input message:')
    ss.sendall(mes)

    data = ss.recv(1024)

    #print 'from server %s' % data
    print data

ss.close()