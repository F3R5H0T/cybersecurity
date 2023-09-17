#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket

s = socket.socket()
try:
	s.connect(("dlptest.com",20))
	banner = s.recv(1024)
	print(banner)
except:
	print("ocurrió un error en la conexión")