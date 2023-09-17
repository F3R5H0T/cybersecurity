#!/usr/bin/env python
#_*_ coding: utf8 _*_

import sys
from shodan import Shodan

reload(sys)
sys.setdefaultencoding('utf8')
key = "S4inbY8uzIl9VDI0aHSLBcmvL1D5R9j8"

def main():
	api = Shodan('S4inbY8uzIl9VDI0aHSLBcmvL1D5R9j8')
	h = api.host('123.57.0.34')
	
	print('''
		Dirección: {}
		Ciudad: {}
		ISp: {}
		Organización: {}
		Puertos: {}
	'''.format(h['ip_str'],h['city'],h['isp'],h['org'],h['ports']))

	for elemento in h['data']:
		lista = elemento.keys()
		for l in lista:
			print(str(elemento[l]))

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()