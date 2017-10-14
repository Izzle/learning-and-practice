import socket

ip = 'enter ip address'
p = 'enter port number'
portList = [21, 22, 80, 110]
portOpen = True
service = {'ftp': 21,
           'ssh': 22,
           'smtp': 25,
           'http': 80}

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)  # The recv method will read the next 1024 bytes on the socket
        return banner
    except:
        print('[-] Error =', str(e))
        return

def checkVuln(banner):
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print('[+] Freefloat FTP server is vulnerable.')
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print('[+] 3CDaemon FTP server is vulnerable.')
    elif 'Ability Server 2.34' in banner:
        print('[+] Ability FTP server is vulnerable.')
    elif 'Sami FTP Server 2.0.2' in banner:
        print('[+] Sami FTP server is vulnerable.')
    else:
        print('[-] FTP server is not vulnerable.')
    return

def example_Try():
    try:
        foo = 'this shouldn\'t print'
        print(foo / 0)
        return
    except Exception, e: #Testing this
        print('[-] Error =', str(e))
        return

example_Try()