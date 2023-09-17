#!/usr/bin/env python
#_*_ coding: utf8 _*_
import dns.resolver

def main():
	consultas = ["A","AAAA",'NS','SOA','MX','TXT','MF']
	for c in consultas:
		try:
			a = dns.resolver.query("google.com",c)
			for q in a:
				print("{}".format(consultas)+": {}".format(q))
		except:
			print("No pude obtener la consulta")
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()