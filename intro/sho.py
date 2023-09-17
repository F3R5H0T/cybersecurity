#!/usr/bin/env python
#_*_ coding: utf8 _*_

import sys
from shodan import Shodan

reload(sys)
sys.setdefaultencoding('utf8')
key = "S4inbY8uzIl9VDI0aHSLBcmvL1D5R9j8"

motor = Shodan(key)

query = motor.search("struts")
print("Total de resultados: {}".format(query['total']))
for host in query['matches']:
	print("IP: {}".format(host['ip_str']))
	print("puerto: {}".format(host['port']))
	print("Organización: {}".format(host['org']))
	try:
		print("ASN: {}".format(host['asn']))
	except: 
		pass
	for l in host['location']:
		print(l+":"+str(host['location'][l]))
	print('\n')
