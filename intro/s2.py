#!/usr/bin/env python
#_*_ coding: utf8 _*_

import sys
from shodan import Shodan
import argparse

reload(sys)
sys.setdefaultencoding('utf8')
key = "S4inbY8uzIl9VDI0aHSLBcmvL1D5R9j8"

parser = argparse.ArgumentParser()
parser.add_argument('-q','--query', help= "Búsqueda")
parser.add_argument('-a','--api',help="Tu api key")
parser = parser.parse_args()

def main():
	if parser.query:
		if parser.api:
			api = Shodan(parser.api)
			try:
				b = api.search(parser.query)
				print("Total de objetivos: {}".format(b['total']))
				for i in b['matches']:
					print("Target encontrad: {}".format(i['ip_str']))

			except:
				print("Error en la consulta")
		else:
			print("introduce tu llave")
	else:
		print("Introduce un carácter de búsqueda")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()