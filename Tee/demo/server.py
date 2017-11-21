import socket

host = '127.0.0.1'
port = 8333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)


while True:

    conn, address = s.accept()


    print conn.recv(1024)

    conn.send('vvv')


