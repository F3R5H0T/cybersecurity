#!/usr/bin/env python
#_*_ coding: utf8 _*_
import urllib2

def main():
	
	#petición sin proxy

	p = urllib2.urlopen('https://ifconfig.me')
	print("IP sin proxy: {}".format(p.read()))

	#configuramos el proxy

	urllib2.install_opener(
		urllib2.build_opener(
			urllib2.ProxyHandler(
				{
					'http':'http://83.96.237.121:80',
					'https':'http://83.96.237.121:80'				
				}

			)
		)
	)

	peticion = urllib2.urlopen("https://ifconfig.me")

	print("IP con proxy: {}".format(peticion.read()))

if __name__ == '__main__':
	main()