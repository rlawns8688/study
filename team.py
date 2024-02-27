#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.27
# modified date  :   2024.02.27
# description  :   

import os
import xmlrpclib
import xmlrpc.client
# Connect to the HQueue server.
hq = xmlrpclib.ServerProxy("http://192.168.5.26:5000")

try:
    hq.runcmd('touch /home/rapa/sangbokkk.txt')
except ConnectionRefusedError:
    print('failed...')


if __name__ == '__main__':
    pass
