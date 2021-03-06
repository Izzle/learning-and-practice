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
        # The recv method will read the next 1024 bytes on the socket
        banner = s.recv(1024)
        return banner
    except Exception as e:
        print('[-] Error =', str(e), '. Error found in retBanner.')
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


'''
   Experimental try except used for experimenting with different ways to handle
   Exceptions. Delete or comment out when the rest of this code is complete.
'''


def example_Try():
    try:
        foo = 'this shouldn\'t print'
        print(foo / 0)
        return
    except Exception as e:
        print('[-] Error =', str(e), '. Error found in example_Try.')
        return

example_Try()
