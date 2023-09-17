#!/usr/bin/env python
#_*_ coding: utf8 _*_

import urllib

def main():
	file_web = open('web.html','w+')
	consulta = urllib.urlopen('https://lorem2.com')
	consulta = consulta.read()
	file_web.write(consulta)
	file_web.close()

if __name__ == '__main__':
	main()