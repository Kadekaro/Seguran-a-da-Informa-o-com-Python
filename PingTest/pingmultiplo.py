import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    for ip in dump:
        print('=' * 80)
        print('Verificando o ip:', ip)
        print('='*80)
        os.system(f'ping -n 2 {ip}')
        print('=' * 80)
        time.sleep(5)