import socket
socket.setdefaulttimeout(2)
s = socket.socket()

ip = 'enter ip address'
p = 'enter port number'
s.connect((ip, p))
ans = s.recv(1024)  # The recv method will read the next 1024 bytes on the socket
portList = [21, 22, 80, 110]
portOpen = True
service = {'ftp': 21,
           'ssh': 22,
           'smtp': 25,
           'http': 80}