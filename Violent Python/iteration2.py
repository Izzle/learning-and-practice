# Violent Python Chapter 1
# This is a continuation of the exercise in iteration.py

import socket


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception:
        return


def checkVulns(banner):
    f = open('vuln_banner.txt', 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print("[+] Server is vulnerable: " + banner.strip('\n'))
        else:
            print('[-] No vulnerable Servers found.')


def main():
    """portList contains all possible vunerable ports we are
      interested in checking: telnet, SSH, smtp, http, imap,
      and https services.
    """
    portList = [21, 22, 25, 80, 110]

    for x in range(1, 255):
        ip = '192.168.95.' + str(x)
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print('[+] ' + ip + ': ' + banner)
                checkVulns(banner)


if __name__ == '__main__':
    main()
