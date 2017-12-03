'''Used for testing security of my Proxmox home lab
   and to verify that things are working correctly.

   TODO: Add threading to speed up the process
'''
import socket
import sys
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Welcome to your Port Scanner')
print('-' * 50)

print('''Please select the format in which you will be entering your data.
      You can select URL or IP.
         example URL: \"www.google.com\"
         example IP: \"192.168.1.1\"
      ''')

answer = input('Enter \"url\" or \"ip\": ')

if answer.lower() == 'url':
    url_answer = input('Enter the url you\'d like to scan: ')
    ip = socket.gethostbyname(url_answer)
    print('URL:', url_answer, 'resolved to IP:', ip)
elif answer.lower() == 'ip':
    ip = input('Enter the ip address you\' like to scan: ')
else:
    print('You dun goofed')
    sys.exit()


time1 = datetime.now()
print('Starting scan @', str(time1))

try:
    for port in range(1, 10000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            print('[+] Port', str(port), 'is open.')
            s.close()
        else:
            print('[-] Port', str(port), 'is closed.')

except KeyboardInterrupt:
    print('You pressed Ctrl+C')
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting..')

except socket.error:
    print('Could not connect to server.')
    sys.exit()

time2 = datetime.now()
duration = time2 - time1
print('Time to complete scan:', str(duration))
